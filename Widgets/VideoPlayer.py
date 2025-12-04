import cv2

from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtCore import Signal, QTimer, Qt
from PySide6.QtGui import QImage, QPixmap

class VideoWidget(QLabel):
    frameChanged   = Signal(int)
    videoFinished  = Signal()
    bookmarkRequested = Signal(float, QPixmap)

    def __init__(self, video_path=None , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame_count = None
        self._original_pixmap = None
        self._last_frame = None
        # Manage None video case
        if video_path:
            self.cap = cv2.VideoCapture(video_path)
            if not self.cap or not self.cap.isOpened():
                raise Exception(f"Cannot open video: {video_path}")
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_frame)
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)

            # Manage the scaling of the video
            self._original_pixmap = None
            self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # Show the first frame
            self.update_frame(force=True)

### Video Time Functions ###
    def Get_total_video_time(self):
        # Get video properties
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.frame_count / self.fps if self.fps > 0 else 0
        return str(self.duration)
    
    def Get_current_video_time(self):
        self.current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        current_time = self.current_frame / self.fps if self.fps > 0 else 0
        return current_time

    def PlayPause_video(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            # Get FPS again if needed
            if self.fps <= 0: # Defoult to 30 if unknown
                self.fps = 30
                print("FPS unknown, defaulting to 30.")
            self.timer.start(int(1000 / self.fps))

    def skip_frame_forward(self, frames=1):
        current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame + frames - 1)
        self.update_frame(force=True)

    def skip_frame_backward(self, frames=1):
        current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame - frames - 1)
        self.update_frame(force=True)

    def get_video_metric(self, arg=None):
        if arg is None:
            return
        elif arg == "Time":
            current_time = self.Get_current_video_time()
            formatted_time = f"{int(current_time // 60):02}:{int(current_time % 60):02}.{int((current_time % 1) * 100):02}"
            return formatted_time
        elif arg == "Frame":
            # Get the current frame number
            frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            return frame
        elif arg == "RT":
            current_time = str(round(self.Get_current_video_time(), 3))
            return current_time

    def update_frame(self, force=False):
        if not self.timer.isActive() and not force:
            return

        if force:
            ret = self.cap.grab()
            if ret:
                ret, frame = self.cap.retrieve()
        else:
            ret, frame = self.cap.read()

        if ret:
            # convert to RGB and wrap in QImage
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Store the last frame for thumbnail use
            self._last_frame = frame.copy()

            # emit signals
            try:
                self.frameChanged.emit(int(self.cap.get(cv2.CAP_PROP_POS_FRAMES)))
            except Exception:
                pass


            # **ONE** setPixmap call—ScaledVideoLabel will auto-scale
            pix = QPixmap.fromImage(q_img)
            self.setPixmap(pix)

    def closeEvent(self, event):
        self.timer.stop()
        if self.cap.isOpened():
            self.cap.release()
        super().closeEvent(event)

    def slider_moved(self, value):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, value)
        self.update_frame(force=True) 

    def set_video_time(self, seconds: float):
        frame_index = int(seconds * self.fps)
        frame_index = max(0, min(frame_index, self.frame_count - 1))
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        self.update_frame(force=True)

    def speed_slider(self, value):
        self.speed_multiplier = value * 0.2
        self.timer.setInterval(int(750 / (self.fps * self.speed_multiplier)))

    def setPixmap(self, pixmap: QPixmap):
        if pixmap is None:
            return
        # store full-size
        self._original_pixmap = pixmap
        # now scale to fit our current widget rect
        scaled = self._original_pixmap.scaled(
            self.size(), 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        super().setPixmap(scaled)

    def resizeEvent(self, ev):
        # whenever we resize, re-scale the last frame
        if self._original_pixmap:
            scaled = self._original_pixmap.scaled(
                ev.size(), 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            super().setPixmap(scaled)
        super().resizeEvent(ev)

    def get_current_frame_pixmap(self, thumb_size: tuple | None = (160, 120)) -> QPixmap | None:
        """Return a QPixmap thumbnail for the current frame."""
        if self._last_frame is not None:
            rgb = self._last_frame  # already RGB from update_frame()
            h, w, ch = rgb.shape
            bytes_per_line = ch * w
            q_img = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888).copy()
            pix = QPixmap.fromImage(q_img)
        else:
            pix = getattr(self, "_original_pixmap", None)
            if pix is None:
                return None

        if thumb_size:
            w, h = thumb_size
            return pix.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return pix