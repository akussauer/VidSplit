from PySide6.QtWidgets import (QMainWindow, QSizePolicy, QLineEdit, QMessageBox, QWidget,
                            QTextEdit, QHeaderView, QDialog, QApplication, QFileDialog)
from PySide6.QtCore import QEvent, Qt
from UI.ui_Video_Splitter import Ui_VideoSplitter
from Widgets.PaintVideo import PaintVideoWidget

class VidSplit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VideoSplitter()

        # Add the UI Visuals
        self.ui.setupUi(self)
        # Connect the UI elements to their respective methods
        self.connect_ui()

    def connect_ui(self):
        # Replace the Video Placeholder
        self.video_widget = PaintVideoWidget(video_path=None)
        self.ui.gridLayout_13.replaceWidget(self.ui.VideoWidget, self.video_widget)
        self.ui.VideoWidget.deleteLater()
        self.video_widget.setMinimumSize(640, 360)
        self.video_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.VideoSlider.setMinimum(0)
        if self.video_widget.frame_count:
            self.ui.VideoSlider.setMaximum(self.video_widget.frame_count - 1)

        # Connect the UI elements to the corresponding methods
        self.ui.actionNew.triggered.connect(self.add_video)

    def eventFilter(self, obj, event):
        try:
            if self.video_widget.frame_count is not None:
                # Define the gap that is between the starts/ends
                self.vid_gap = 2.0 # seconds
                
                if event.type() == QEvent.KeyPress:
                    key = event.key()
                    modifiers = event.modifiers()

                    if modifiers == Qt.NoModifier:
                        if key == Qt.Key_Space:
                            self.video_widget.PlayPause_video()
                            return True
                        if key == Qt.Key_Right:
                            self.video_widget.skip_frame_forward(10)
                            return True
                        elif key == Qt.Key_Left:
                            self.video_widget.skip_frame_backward(10)
                            return True
                        elif key == Qt.Key_S:
                            focus = self.focusWidget()
                            if isinstance(focus, QLineEdit):
                                name = focus.objectName()
                                if name.startswith("Start"):
                                    # Get the entry time and insert it
                                    time_s = self.video_widget.Get_current_video_time()
                                    time = self.parse_seconds_to_time(time_s)
                                    if time is not None:
                                        focus.setText(time)
                                        focus.focusNextPrevChild(True)
                                        return True
                                    
                                if name.startswith("End"):
                                    # Get the entry time and insert it
                                    time_s = self.video_widget.Get_current_video_time()
                                    time = self.parse_seconds_to_time(time_s)
                                    if time is not None:
                                        focus.setText(time)
                                        focus.focusNextPrevChild(True)
                                    # Fill the overlapping end time if empty
                                    if int(name[-1]) >= 1 and int(name[-1]) < 4:
                                        end = self.findChild(QLineEdit, f"StartLE_{(int(name[-1])+1)}")
                                        if end:
                                            end.setText(time)
                                            focus.focusNextPrevChild(True)    
                                            return True 

                    elif modifiers == Qt.ShiftModifier:
                        if key == Qt.Key_Right:
                            self.video_widget.skip_frame_forward(35)
                            return True
                        elif key == Qt.Key_Left:
                            self.video_widget.skip_frame_backward(35)
                            return True
                
        except Exception as e:
            print(f"Error in eventFilter: {e}")
        return super().eventFilter(obj, event)

    def add_video(self):
        # Add the video to the application
        video_file, _ = QFileDialog.getOpenFileName(self,
                                                 "Open Video File", "", "Video Files (*.mp4 *.MP4 *.avi *.AVI *.mov *.MOV *.mkv *.MKV *.mts *.MTS)")
        if video_file:
            try:
                new_video_widget = PaintVideoWidget(video_path=video_file)
                self.ui.gridLayout_13.replaceWidget(self.video_widget, new_video_widget)
                self.video_widget.deleteLater()
                self.video_widget = new_video_widget
                self.video_widget.setMinimumSize(640, 360)
                self.video_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.ui.VideoSlider.setMinimum(0)
                if self.video_widget.frame_count:
                    self.ui.VideoSlider.setMaximum(self.video_widget.frame_count - 1)
                
                # Connect the UI
                self.ui.PlayPauseButton.clicked.connect(self.video_widget.PlayPause_video)
                self.ui.VideoSlider.valueChanged.connect(self.video_widget.slider_moved)
                self.video_widget.frameChanged.connect(self.update_video_labels)

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load video: {e}")
                print(f"Error loading video: {e}") 

    def update_video_labels(self, frame_index: int):
        # Update the labels with the current frame index and time
        current_time = self.video_widget.get_video_metric(arg="Time")
        self.ui.CurrentTimeLabel.setText(current_time)
        self.ui.EndTimeLabel.setText(self.parse_seconds_to_time(self.video_widget.Get_total_video_time()))

        self.ui.VideoSlider.blockSignals(True)
        self.ui.VideoSlider.setValue(frame_index)
        self.ui.VideoSlider.blockSignals(False)

    def parse_seconds_to_time(self, seconds):
        if seconds is None:
            return ""
        # Ensure seconds is a str
        seconds = str(seconds)
        # Parse seconds by "."
        if "." in seconds:
            seconds, hundredths = seconds.split(".")
            hundredths = hundredths[:2]

        minutes = (int(seconds) // 60)
        seconds = (int(seconds) % 60)
        return f"{minutes:02}:{seconds:02}.{hundredths:02}"

# Run the application (This can be removed later if integrating into a larger app)
if __name__ == "__main__":
    app = QApplication([])
    window = VidSplit()
    QApplication.instance().installEventFilter(window) # Install the event filter (for hotkeys)
    window.show()
    app.exec()
