# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideSplitmfldBw.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QWidget)

class Ui_VideoSplitter(object):
    def setupUi(self, VideoSplitter):
        if not VideoSplitter.objectName():
            VideoSplitter.setObjectName(u"VideoSplitter")
        VideoSplitter.resize(1074, 600)
        icon = QIcon()
        icon.addFile(u"Resources/bread.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        VideoSplitter.setWindowIcon(icon)
        self.actionSave = QAction(VideoSplitter)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(VideoSplitter)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExport_PDF = QAction(VideoSplitter)
        self.actionExport_PDF.setObjectName(u"actionExport_PDF")
        self.actionNew = QAction(VideoSplitter)
        self.actionNew.setObjectName(u"actionNew")
        self.centralwidget = QWidget(VideoSplitter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.ContainerUpper = QWidget(self.centralwidget)
        self.ContainerUpper.setObjectName(u"ContainerUpper")
        self.gridLayout_13 = QGridLayout(self.ContainerUpper)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.scrollArea = QScrollArea(self.ContainerUpper)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QSize(250, 16777215))
        self.scrollArea.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 246, 466))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.AthleteGB_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.AthleteGB_4.setObjectName(u"AthleteGB_4")
        self.gridLayout_6 = QGridLayout(self.AthleteGB_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(4)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(8, 0, 8, 5)
        self.EndLE_4 = QLineEdit(self.AthleteGB_4)
        self.EndLE_4.setObjectName(u"EndLE_4")

        self.gridLayout_6.addWidget(self.EndLE_4, 1, 2, 1, 1)

        self.End_label_4 = QLabel(self.AthleteGB_4)
        self.End_label_4.setObjectName(u"End_label_4")

        self.gridLayout_6.addWidget(self.End_label_4, 0, 2, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.Start_label_4 = QLabel(self.AthleteGB_4)
        self.Start_label_4.setObjectName(u"Start_label_4")

        self.gridLayout_6.addWidget(self.Start_label_4, 0, 1, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.StartLE_4 = QLineEdit(self.AthleteGB_4)
        self.StartLE_4.setObjectName(u"StartLE_4")

        self.gridLayout_6.addWidget(self.StartLE_4, 1, 1, 1, 1)

        self.TimeLE_4 = QLineEdit(self.AthleteGB_4)
        self.TimeLE_4.setObjectName(u"TimeLE_4")

        self.gridLayout_6.addWidget(self.TimeLE_4, 1, 0, 1, 1)

        self.TimeLabel_4 = QLabel(self.AthleteGB_4)
        self.TimeLabel_4.setObjectName(u"TimeLabel_4")

        self.gridLayout_6.addWidget(self.TimeLabel_4, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.AthleteGB_4, 8, 0, 1, 1)

        self.GapContainer = QWidget(self.scrollAreaWidgetContents)
        self.GapContainer.setObjectName(u"GapContainer")
        self.gridLayout_3 = QGridLayout(self.GapContainer)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(8, 4, 8, 2)
        self.GapLabel = QLabel(self.GapContainer)
        self.GapLabel.setObjectName(u"GapLabel")

        self.gridLayout_3.addWidget(self.GapLabel, 0, 0, 1, 1)

        self.GapSB = QDoubleSpinBox(self.GapContainer)
        self.GapSB.setObjectName(u"GapSB")
        self.GapSB.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.GapSB.setMinimum(1.000000000000000)
        self.GapSB.setValue(2.500000000000000)

        self.gridLayout_3.addWidget(self.GapSB, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.GapContainer, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.AthleteGB_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.AthleteGB_2.setObjectName(u"AthleteGB_2")
        self.gridLayout_4 = QGridLayout(self.AthleteGB_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(4)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(8, 0, 8, 5)
        self.EndLE_2 = QLineEdit(self.AthleteGB_2)
        self.EndLE_2.setObjectName(u"EndLE_2")

        self.gridLayout_4.addWidget(self.EndLE_2, 1, 2, 1, 1)

        self.Start_label_2 = QLabel(self.AthleteGB_2)
        self.Start_label_2.setObjectName(u"Start_label_2")

        self.gridLayout_4.addWidget(self.Start_label_2, 0, 1, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.End_label_2 = QLabel(self.AthleteGB_2)
        self.End_label_2.setObjectName(u"End_label_2")

        self.gridLayout_4.addWidget(self.End_label_2, 0, 2, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.StartLE_2 = QLineEdit(self.AthleteGB_2)
        self.StartLE_2.setObjectName(u"StartLE_2")

        self.gridLayout_4.addWidget(self.StartLE_2, 1, 1, 1, 1)

        self.TimeLE_2 = QLineEdit(self.AthleteGB_2)
        self.TimeLE_2.setObjectName(u"TimeLE_2")

        self.gridLayout_4.addWidget(self.TimeLE_2, 1, 0, 1, 1)

        self.TimeLabel_2 = QLabel(self.AthleteGB_2)
        self.TimeLabel_2.setObjectName(u"TimeLabel_2")

        self.gridLayout_4.addWidget(self.TimeLabel_2, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.AthleteGB_2, 6, 0, 1, 1)

        self.SplitVidButton = QPushButton(self.scrollAreaWidgetContents)
        self.SplitVidButton.setObjectName(u"SplitVidButton")

        self.gridLayout_7.addWidget(self.SplitVidButton, 11, 0, 1, 1)

        self.AthleteGB_1 = QGroupBox(self.scrollAreaWidgetContents)
        self.AthleteGB_1.setObjectName(u"AthleteGB_1")
        self.gridLayout = QGridLayout(self.AthleteGB_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(8, 0, 8, 5)
        self.End_label_1 = QLabel(self.AthleteGB_1)
        self.End_label_1.setObjectName(u"End_label_1")

        self.gridLayout.addWidget(self.End_label_1, 0, 2, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.StartLE_1 = QLineEdit(self.AthleteGB_1)
        self.StartLE_1.setObjectName(u"StartLE_1")
        self.StartLE_1.setEnabled(True)

        self.gridLayout.addWidget(self.StartLE_1, 1, 1, 1, 1)

        self.Start_label_1 = QLabel(self.AthleteGB_1)
        self.Start_label_1.setObjectName(u"Start_label_1")

        self.gridLayout.addWidget(self.Start_label_1, 0, 1, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.EndLE_1 = QLineEdit(self.AthleteGB_1)
        self.EndLE_1.setObjectName(u"EndLE_1")
        self.EndLE_1.setEnabled(True)

        self.gridLayout.addWidget(self.EndLE_1, 1, 2, 1, 1)

        self.TimeLabel_1 = QLabel(self.AthleteGB_1)
        self.TimeLabel_1.setObjectName(u"TimeLabel_1")

        self.gridLayout.addWidget(self.TimeLabel_1, 0, 0, 1, 1)

        self.TimeLE_1 = QLineEdit(self.AthleteGB_1)
        self.TimeLE_1.setObjectName(u"TimeLE_1")

        self.gridLayout.addWidget(self.TimeLE_1, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.AthleteGB_1, 5, 0, 1, 1)

        self.AthleteGB_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.AthleteGB_3.setObjectName(u"AthleteGB_3")
        self.gridLayout_5 = QGridLayout(self.AthleteGB_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(4)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(8, 0, 8, 5)
        self.EndLE_3 = QLineEdit(self.AthleteGB_3)
        self.EndLE_3.setObjectName(u"EndLE_3")

        self.gridLayout_5.addWidget(self.EndLE_3, 1, 2, 1, 1)

        self.End_label_3 = QLabel(self.AthleteGB_3)
        self.End_label_3.setObjectName(u"End_label_3")

        self.gridLayout_5.addWidget(self.End_label_3, 0, 2, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.StartLE_3 = QLineEdit(self.AthleteGB_3)
        self.StartLE_3.setObjectName(u"StartLE_3")

        self.gridLayout_5.addWidget(self.StartLE_3, 1, 1, 1, 1)

        self.Start_label_3 = QLabel(self.AthleteGB_3)
        self.Start_label_3.setObjectName(u"Start_label_3")

        self.gridLayout_5.addWidget(self.Start_label_3, 0, 1, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.TimeLE_3 = QLineEdit(self.AthleteGB_3)
        self.TimeLE_3.setObjectName(u"TimeLE_3")

        self.gridLayout_5.addWidget(self.TimeLE_3, 1, 0, 1, 1)

        self.TimeLabel_3 = QLabel(self.AthleteGB_3)
        self.TimeLabel_3.setObjectName(u"TimeLabel_3")

        self.gridLayout_5.addWidget(self.TimeLabel_3, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.AthleteGB_3, 7, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_13.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.VideoWidget = QWidget(self.ContainerUpper)
        self.VideoWidget.setObjectName(u"VideoWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.VideoWidget.sizePolicy().hasHeightForWidth())
        self.VideoWidget.setSizePolicy(sizePolicy1)
        self.VideoWidget.setMouseTracking(True)

        self.gridLayout_13.addWidget(self.VideoWidget, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.ContainerUpper, 0, 0, 1, 1)

        self.AnalysisMediaContainerOuter = QWidget(self.centralwidget)
        self.AnalysisMediaContainerOuter.setObjectName(u"AnalysisMediaContainerOuter")
        self.AnalysisMediaContainerOuter.setMaximumSize(QSize(16777215, 79))
        self.gridLayout_12 = QGridLayout(self.AnalysisMediaContainerOuter)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(-1, 5, 9, 5)
        self.AnalysisVideoContainerInner = QWidget(self.AnalysisMediaContainerOuter)
        self.AnalysisVideoContainerInner.setObjectName(u"AnalysisVideoContainerInner")
        self.gridLayout_11 = QGridLayout(self.AnalysisVideoContainerInner)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(179, 19, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(179, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.AnalysisContainerButtons = QWidget(self.AnalysisVideoContainerInner)
        self.AnalysisContainerButtons.setObjectName(u"AnalysisContainerButtons")
        self.gridLayout_8 = QGridLayout(self.AnalysisContainerButtons)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(10)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.PlayPauseButton = QPushButton(self.AnalysisContainerButtons)
        self.PlayPauseButton.setObjectName(u"PlayPauseButton")
        self.PlayPauseButton.setMinimumSize(QSize(45, 30))
        self.PlayPauseButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.PlayPauseButton.setMouseTracking(False)
        self.PlayPauseButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.PlayPauseButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u"Resources/pause-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PlayPauseButton.setIcon(icon1)
        self.PlayPauseButton.setCheckable(True)
        self.PlayPauseButton.setChecked(False)

        self.gridLayout_8.addWidget(self.PlayPauseButton, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.CurrentTimeLabel = QLabel(self.AnalysisContainerButtons)
        self.CurrentTimeLabel.setObjectName(u"CurrentTimeLabel")
        font = QFont()
        font.setBold(True)
        self.CurrentTimeLabel.setFont(font)
        self.CurrentTimeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.CurrentTimeLabel, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.AnalysisContainerButtons, 0, 2, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.EndTimeLabel = QLabel(self.AnalysisVideoContainerInner)
        self.EndTimeLabel.setObjectName(u"EndTimeLabel")

        self.gridLayout_11.addWidget(self.EndTimeLabel, 0, 4, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.StartTimeLabel = QLabel(self.AnalysisVideoContainerInner)
        self.StartTimeLabel.setObjectName(u"StartTimeLabel")

        self.gridLayout_11.addWidget(self.StartTimeLabel, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.gridLayout_12.addWidget(self.AnalysisVideoContainerInner, 1, 0, 1, 1)

        self.VideoSlider = QSlider(self.AnalysisMediaContainerOuter)
        self.VideoSlider.setObjectName(u"VideoSlider")
        self.VideoSlider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.VideoSlider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.VideoSlider.setMaximum(10000000)
        self.VideoSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_12.addWidget(self.VideoSlider, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.AnalysisMediaContainerOuter, 1, 0, 1, 1)

        VideoSplitter.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(VideoSplitter)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1074, 33))
        self.menuBar.setMaximumSize(QSize(16777215, 16777215))
        self.menuNew = QMenu(self.menuBar)
        self.menuNew.setObjectName(u"menuNew")
        self.menuNew.setTearOffEnabled(False)
        VideoSplitter.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.GapSB, self.TimeLE_1)
        QWidget.setTabOrder(self.TimeLE_1, self.StartLE_1)
        QWidget.setTabOrder(self.StartLE_1, self.EndLE_1)
        QWidget.setTabOrder(self.EndLE_1, self.TimeLE_2)
        QWidget.setTabOrder(self.TimeLE_2, self.StartLE_2)
        QWidget.setTabOrder(self.StartLE_2, self.EndLE_2)
        QWidget.setTabOrder(self.EndLE_2, self.TimeLE_3)
        QWidget.setTabOrder(self.TimeLE_3, self.StartLE_3)
        QWidget.setTabOrder(self.StartLE_3, self.EndLE_3)
        QWidget.setTabOrder(self.EndLE_3, self.TimeLE_4)
        QWidget.setTabOrder(self.TimeLE_4, self.StartLE_4)
        QWidget.setTabOrder(self.StartLE_4, self.EndLE_4)
        QWidget.setTabOrder(self.EndLE_4, self.SplitVidButton)

        self.menuBar.addAction(self.menuNew.menuAction())
        self.menuNew.addAction(self.actionNew)

        self.retranslateUi(VideoSplitter)

        QMetaObject.connectSlotsByName(VideoSplitter)
    # setupUi

    def retranslateUi(self, VideoSplitter):
        VideoSplitter.setWindowTitle(QCoreApplication.translate("VideoSplitter", u"Video Slicer", None))
        self.actionSave.setText(QCoreApplication.translate("VideoSplitter", u"New", None))
        self.actionSave_As.setText(QCoreApplication.translate("VideoSplitter", u"Save As", None))
        self.actionExport_PDF.setText(QCoreApplication.translate("VideoSplitter", u"Export PDF", None))
        self.actionNew.setText(QCoreApplication.translate("VideoSplitter", u"New...", None))
        self.AthleteGB_4.setTitle(QCoreApplication.translate("VideoSplitter", u"Athlete 4", None))
        self.EndLE_4.setInputMask(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.End_label_4.setText(QCoreApplication.translate("VideoSplitter", u"End", None))
        self.Start_label_4.setText(QCoreApplication.translate("VideoSplitter", u"Start", None))
        self.StartLE_4.setInputMask(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.TimeLE_4.setInputMask(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.TimeLabel_4.setText(QCoreApplication.translate("VideoSplitter", u"Time", None))
        self.GapLabel.setText(QCoreApplication.translate("VideoSplitter", u"Gap (s)", None))
        self.AthleteGB_2.setTitle(QCoreApplication.translate("VideoSplitter", u"Athlete 2", None))
        self.EndLE_2.setInputMask(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.Start_label_2.setText(QCoreApplication.translate("VideoSplitter", u"Start", None))
        self.End_label_2.setText(QCoreApplication.translate("VideoSplitter", u"End", None))
        self.StartLE_2.setInputMask(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.TimeLE_2.setInputMask(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.TimeLabel_2.setText(QCoreApplication.translate("VideoSplitter", u"Time", None))
        self.SplitVidButton.setText(QCoreApplication.translate("VideoSplitter", u"Split Video", None))
        self.AthleteGB_1.setTitle(QCoreApplication.translate("VideoSplitter", u"Athlete 1", None))
        self.End_label_1.setText(QCoreApplication.translate("VideoSplitter", u"End", None))
        self.StartLE_1.setInputMask(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.Start_label_1.setText(QCoreApplication.translate("VideoSplitter", u"Start", None))
        self.EndLE_1.setInputMask(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.TimeLabel_1.setText(QCoreApplication.translate("VideoSplitter", u"Time", None))
        self.TimeLE_1.setInputMask(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.AthleteGB_3.setTitle(QCoreApplication.translate("VideoSplitter", u"Athlete 3", None))
        self.EndLE_3.setInputMask(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.End_label_3.setText(QCoreApplication.translate("VideoSplitter", u"End", None))
        self.StartLE_3.setInputMask(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.Start_label_3.setText(QCoreApplication.translate("VideoSplitter", u"Start", None))
        self.TimeLE_3.setInputMask(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.TimeLabel_3.setText(QCoreApplication.translate("VideoSplitter", u"Time", None))
        self.CurrentTimeLabel.setText(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.EndTimeLabel.setText(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.StartTimeLabel.setText(QCoreApplication.translate("VideoSplitter", u"00:00.00", None))
        self.menuNew.setTitle(QCoreApplication.translate("VideoSplitter", u"File", None))
    # retranslateUi

