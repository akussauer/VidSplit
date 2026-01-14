import re
import os
import platform
from PySide6.QtWidgets import (QMainWindow, QSizePolicy, QLineEdit, QMessageBox, QApplication, QFileDialog)
from PySide6.QtCore import QEvent, Qt, QProcess
from UI.ui_Video_Splitter import Ui_VideoSplitter
from Widgets.VideoPlayer import VideoWidget

class VidSplit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VideoSplitter()

        self.video_file = None
        self.process = None
        self.current_output_path = None
        self.total_frames = None
        self.fps = None

        # Add the UI Visuals
        self.ui.setupUi(self)
        # Connect the UI elements to their respective methods
        self.connect_ui()

        # Setup ffmpeg path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if platform.system() == "Windows":
            self.ffmpeg_path = os.path.join(base_dir, "ffmpeg", "ffmpeg.exe")
        else:
            self.ffmpeg_path = os.path.join(base_dir, "ffmpeg", "ffmpeg")

        # Check ffmpeg path
        if not self.ffmpeg_path or not os.path.exists(self.ffmpeg_path):
            QMessageBox.critical(self, f"FFmpeg Not Found in {self.ffmpeg_path}", "FFmpeg executable not found. Please ensure ffmpeg is included in the application directory.")
            self.ffmpeg_path = None

    def connect_ui(self):
        # Replace the Video Placeholder
        self.video_widget = VideoWidget(video_path=None)
        self.ui.gridLayout_13.replaceWidget(self.ui.VideoWidget, self.video_widget)
        self.ui.VideoWidget.deleteLater()
        self.video_widget.setMinimumSize(640, 360)
        self.video_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.VideoSlider.setMinimum(0)
        if self.video_widget.frame_count:
            self.ui.VideoSlider.setMaximum(self.video_widget.frame_count - 1)
        # Disable parts of the UI until a video is loaded
        self.ui.PlayPauseButton.setEnabled(False)
        self.ui.VideoSlider.setEnabled(False)

        # Connect the UI elements to the corresponding methods
        self.ui.actionNew.triggered.connect(self.add_video)
        self.ui.SplitVidButton.clicked.connect(self.start_video_split)

    def eventFilter(self, obj, event):
        try:
            if self.video_widget.frame_count is not None:
                # Define the gap that is between the starts/ends
                vid_gap = self.ui.GapSB.value()
                
                if event.type() == QEvent.KeyPress:
                    key = event.key()
                    modifiers = event.modifiers()

                    if modifiers == Qt.NoModifier:
                        if key == Qt.Key_Space:
                            self.video_widget.PlayPause_video()
                            return True
                        if key == Qt.Key_Right:
                            self.video_widget.skip_frame_forward(20)
                            return True
                        elif key == Qt.Key_Left:
                            self.video_widget.skip_frame_backward(20)
                            return True
                        elif key == Qt.Key_S:
                            focus = self.focusWidget()
                            if isinstance(focus, QLineEdit):
                                name = focus.objectName()
                                if name.startswith("Time"):
                                    # Get the entry time and insert it
                                    time_s = self.video_widget.Get_current_video_time()
                                    time = self.parse_seconds_to_time(time_s)
                                    if time is not None:
                                        focus.setText(time)
                                    
                                    if int(name[-1]) > 0:
                                        start_time_s = time_s - vid_gap
                                        if start_time_s < 0:
                                            start_time_s = 0.0

                                        start_time = self.parse_seconds_to_time(start_time_s)
                                        # Handle the StartLE_x entries
                                        start = self.findChild(QLineEdit, f"StartLE_{(int(name[-1]))}")
                                        if start:
                                            start.setText(start_time)
                                            # Set focus to the next TimeLE_x entry
                                            if int(name[-1]) < 4:
                                                next_time = self.findChild(QLineEdit, f"TimeLE_{(int(name[-1])+1)}")
                                                if next_time:
                                                    next_time.setFocus()
                                            elif int(name[-1]) == 4:
                                                end = self.findChild(QLineEdit, f"EndLE_{(int(name[-1]))}")
                                                if end:
                                                    end.setFocus()
                                        
                                        # Handle the EndLE_x entries
                                        end = self.findChild(QLineEdit, f"EndLE_{(int(name[-1])-1)}")
                                        if end:
                                            end_time_s = time_s + vid_gap
                                            if end_time_s > float(self.video_widget.Get_total_video_time()):
                                                end_time_s = time_s
                                            end_time = self.parse_seconds_to_time(end_time_s)
                                            end.setText(end_time)
                                
                                        return True
                                elif name.startswith("Start") or name.startswith("End"):
                                    time_s = self.video_widget.Get_current_video_time()
                                    time = self.parse_seconds_to_time(time_s)
                                    if time is not None:
                                        focus.setText(time)
                                        focus.focusNextPrevChild(True)
                                    return True

                    elif modifiers == Qt.ShiftModifier:
                        if key == Qt.Key_Right:
                            self.video_widget.skip_frame_forward(50)
                            return True
                        elif key == Qt.Key_Left:
                            self.video_widget.skip_frame_backward(50)
                            return True
                
        except Exception as e:
            print(f"Error in eventFilter: {e}")
        return super().eventFilter(obj, event)

    def add_video(self):
        # Add the video to the application
        self.video_file, _ = QFileDialog.getOpenFileName(self,
                                                 "Open Video File", "", "Video Files (*.mp4 *.MP4 *.avi *.AVI *.mov *.MOV *.mkv *.MKV *.mts *.MTS)")
        if self.video_file:
            try:
                new_video_widget = VideoWidget(video_path=self.video_file)
                self.ui.gridLayout_13.replaceWidget(self.video_widget, new_video_widget)
                self.video_widget.deleteLater()
                self.video_widget = new_video_widget
                self.video_widget.setMinimumSize(640, 360)
                self.video_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.ui.VideoSlider.setMinimum(0)
                if self.video_widget.frame_count:
                    self.ui.VideoSlider.setMaximum(self.video_widget.frame_count - 1)

                # Enable the UI now that a video is loaded
                self.ui.PlayPauseButton.setEnabled(True)
                self.ui.VideoSlider.setEnabled(True)
                
                # Connect the UI
                self.ui.PlayPauseButton.clicked.connect(self.video_widget.PlayPause_video)
                self.ui.VideoSlider.valueChanged.connect(self.video_widget.slider_moved)
                self.video_widget.frameChanged.connect(self.update_video_labels)

            # Clear all the LineEdits
                for i in range(0, 6):
                    start_le = self.findChild(QLineEdit, f"StartLE_{i}")
                    end_le = self.findChild(QLineEdit, f"EndLE_{i}")
                    time_le = self.findChild(QLineEdit, f"TimeLE_{i}")
                    if start_le:
                        start_le.clear()
                    if end_le:
                        end_le.clear()
                    if time_le:
                        time_le.clear()

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
    
    def parse_time_to_seconds(self, time_str):
        try:
            time_str = time_str.strip()

            if not time_str or time_str in [".", ",", ":.", None]:
                return None  # Incomplete or invalid input

            # If input matches mm:ss.xx
            match = re.match(r"^(\d{1,2}):(\d{2})(?:\.(\d{1,2}))?$", time_str)
            if match:
                minutes = float(match.group(1))
                seconds = float(match.group(2))
                hundredths = float(match.group(3)) if match.group(3) else 0
                return (minutes * 60) + seconds + (hundredths / 100.0)

            if time_str is None or time_str == "" or str(time_str).strip().lower() == "none":
                return None

            # Otherwise, try to parse it directly as seconds
            return float(time_str)

        except ValueError:
            return None

    def start_video_split(self):
        if not self.video_file:
            QMessageBox.warning(self, "No Video", "Please load a video before starting the split.")
            return

        output_dir = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if not output_dir:
            return
        
        # Change the cursor to busy
        QApplication.setOverrideCursor(Qt.WaitCursor)
        QApplication.processEvents()
        
        def sanitize_path(path: str) -> str:
            # Split path into parts
            parts = path.replace("\\", "/").split("/")
            # Remove control characters from each part
            clean_parts = [re.sub(r"[\x00-\x1f\x7f]", "", p) for p in parts]
            # Reassemble into safe path
            return "/".join(clean_parts)

        # Build the segment list
        self.segment_queue = []
        for i in range(0, 6):
            start_le = self.findChild(QLineEdit, f"StartLE_{i}")
            end_le = self.findChild(QLineEdit, f"EndLE_{i}")
            if start_le and end_le:
                start = self.parse_time_to_seconds(start_le.text().strip())
                end = self.parse_time_to_seconds(end_le.text().strip())
                if start is None or end is None:
                    continue
                if start is not None and end is not None:
                    input_path = sanitize_path(self.video_file)
                    output_dir = sanitize_path(output_dir)

                    file = os.path.basename(input_path)
                    name, ext = os.path.splitext(file)
                    name = re.sub(r"[\x00-\x1f\x7f]", "", name)

                    output_path = sanitize_path(os.path.join(output_dir, f"{name}_{i}{ext}"))
                    # Check if output file already exists
                    if os.path.exists(output_path):
                        output_path = sanitize_path(os.path.join(output_dir, f"{name}_{i}(1){ext}"))
                    self.segment_queue.append((start, end, output_path))

        if not self.segment_queue:
            QMessageBox.warning(self, "No Segments", "No valid start/end times entered.")
            return
        
        self.start_next_segment()

    def start_next_segment(self):
        if not self.segment_queue:
            QApplication.restoreOverrideCursor()
            QMessageBox.information(self, "Completed", "All video segments have been processed.")
            return
        
        def seconds_to_timestamp(secs):
            secs = float(secs)
            h = int(secs // 3600)
            m = int((secs % 3600) // 60)
            s = secs % 60
            return f"{h:02d}:{m:02d}:{s:05.2f}"

        start, end, output_path = self.segment_queue.pop(0)

        start_s = seconds_to_timestamp(start)
        end_s = seconds_to_timestamp(end)
        self.start_process(self.video_file, output_path, start_time=start_s, end_time=end_s)

## Video Transcoding Section ##
    def start_process(self, input_path, output_path, start_time=None, end_time=None):
        # ensure no leftover process (if one exists and is running, we don't kill it here - that should be avoided)
        if self.process is not None and self.process.state() != QProcess.NotRunning:
            try:
                # very defensive: normally shouldn't happen because transcode_next_video avoids starting twice
                self.process.kill()
                print("Killed existing ffmpeg process.")
            except Exception:
                pass

        try:
            # store output path so process_finished can reference & delete on failure
            self.current_output_path = output_path

            self.process = QProcess()
            self.process.readyReadStandardOutput.connect(self.handle_stdout)
            self.process.readyReadStandardError.connect(self.handle_stderr)
            self.process.stateChanged.connect(self.handle_state)
            # accept parameters from finished signal (exitCode, exitStatus)
            # QProcess.finished -> (int, QProcess.ExitStatus)
            self.process.finished.connect(self.process_finished)

            # Start ffmpeg
            if self.ffmpeg_path is None or not os.path.exists(self.ffmpeg_path):
                print("FFmpeg executable not found.")
                self.process = None
                return False

            self.process.start(
                self.ffmpeg_path,
                ["-ss", str(start_time), "-to", str(end_time), "-i", input_path, "-c", "copy", output_path]
            )

        except Exception as e:
            QMessageBox.critical(self, "FFmpeg Failure", f"Failed to start video processing: {str(e)}")
            print(f"Error starting ffmpeg process: {e}")

            self.process = None
            return False
    
    def handle_stdout(self):
        # not used for progress but left in case you want to capture ffmpeg stdout
        _ = bytes(self.process.readAllStandardOutput()).decode('utf-8', errors='ignore')

    def handle_stderr(self):
        # Parse ffmpeg stderr incrementally to extract duration, fps, and frame progress
        data = bytes(self.process.readAllStandardError()).decode('utf-8', errors='ignore')
        if not data:
            return

        # Try to parse duration (once)
        if self.total_frames is None:
            duration_match = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", data)
            if duration_match:
                h, m, s = duration_match.groups()
                self.duration_seconds = float(h) * 3600 + float(m) * 60 + float(s)

            # fps can appear as "30 fps" or "30.00 fps"
            fps_match = re.search(r"(\d+(?:\.\d+)?)\s+fps", data)
            if fps_match:
                try:
                    self.fps = float(fps_match.group(1))
                except Exception:
                    self.fps = None

            if getattr(self, "duration_seconds", None) and getattr(self, "fps", None):
                # small safety checks
                try:
                    est = int(self.duration_seconds * self.fps)
                    # apply your empirical correction factor (optional)
                    self.total_frames = max(1, int(est * 0.6))
                except Exception:
                    self.total_frames = None

        # parse 'frame=   123' style output (ffmpeg prints repeated frames)
        frame_match = re.search(r"frame=\s*(\d+)", data)
        if frame_match:
            try:
                frame_number = int(frame_match.group(1))
            except Exception:
                frame_number = 0

            # compute progress if we have a total_frames estimate
            progress = 0
            if self.total_frames and self.total_frames > 0:
                progress = int(frame_number / float(self.total_frames) * 100)
                if progress > 99:
                    # leave final 100% for process_finished
                    progress = 99
            else:
                # fallback: if no total frames, you could attempt to use time-based or just show spinner
                progress = 0

    def handle_state(self, state):
        # Handle the state of the process
        states = {
            QProcess.NotRunning: "Not Running",
            QProcess.Starting: "Starting",
            QProcess.Running: "Running",
        }
        self.transcoding_state = states[state]

    def process_finished(self, exit_code, exit_status):
        if exit_code == 0 and exit_status == QProcess.NormalExit:
            pass # Successful completion - nothing special to do
        else:
            print(f"Segment failed: exit {exit_code}, status {exit_status}")
            if self.current_output_path and os.path.exists(self.current_output_path):
                os.remove(self.current_output_path)

        # Reset state
        self.process = None
        self.current_output_path = None
        self.total_frames = None
        self.fps = None
        self.duration_seconds = None

        # Start the next video in the queue
        self.start_next_segment()

# Run the application (This can be removed later if integrating into a larger app)
if __name__ == "__main__":
    app = QApplication([])
    window = VidSplit()
    QApplication.instance().installEventFilter(window) # Install the event filter (for hotkeys)
    window.show()
    app.exec()