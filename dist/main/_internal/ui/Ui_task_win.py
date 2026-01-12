# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_win.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import rec_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(236, 335)
        Form.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        Form.setWindowOpacity(0.700000000000000)
        Form.setStyleSheet(u"")
        self.frame_9 = QFrame(Form)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(1, 4, 233, 329))
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 215, 93);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_9)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 230, 186))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(5, 10, 40, 160))
        self.frame_7.setMinimumSize(QSize(40, 160))
        self.frame_7.setMaximumSize(QSize(40, 160))
        self.frame_7.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left: 6px;\n"
"    padding-top: 6px;\n"
"    padding-right: 2px;\n"
"    padding-bottom: 2px;\n"
"\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_7)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(36, 36))
        self.pushButton_5.setMaximumSize(QSize(36, 36))
        font = QFont()
        font.setFamilies([u"\u96b6\u4e66"])
        font.setPointSize(13)
        self.pushButton_5.setFont(font)
        icon = QIcon()
        icon.addFile(u":/res/icon/list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(36)
        sizePolicy.setVerticalStretch(36)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QSize(36, 36))
        self.pushButton_6.setMaximumSize(QSize(36, 36))
        self.pushButton_6.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/res/icon/weather.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(36, 36))
        self.pushButton_7.setMaximumSize(QSize(36, 36))
        self.pushButton_7.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/res/icon/word.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QSize(36, 36))
        self.pushButton_8.setMaximumSize(QSize(36, 36))
        self.pushButton_8.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_8)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(50, 0, 182, 186))
        self.stackedWidget.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 180, 184))
        self.frame_2.setMinimumSize(QSize(180, 180))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	border: 1px solid #00c8ff;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(178, 60))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_evening_1 = QCheckBox(self.frame_3)
        self.checkBox_evening_1.setObjectName(u"checkBox_evening_1")
        self.checkBox_evening_1.setMinimumSize(QSize(176, 16))
        self.checkBox_evening_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.checkBox_evening_1, 1, 0, 1, 1)

        self.checkBox_evening_2 = QCheckBox(self.frame_3)
        self.checkBox_evening_2.setObjectName(u"checkBox_evening_2")
        self.checkBox_evening_2.setMinimumSize(QSize(176, 16))
        self.checkBox_evening_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.checkBox_evening_2, 2, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font1 = QFont()
        font1.setStrikeOut(False)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButton_3.setStyleSheet(u"#pushButton_3{\n"
"	border:none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/res/icon/night.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(178, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox_afternoon_1 = QCheckBox(self.frame_4)
        self.checkBox_afternoon_1.setObjectName(u"checkBox_afternoon_1")
        self.checkBox_afternoon_1.setMinimumSize(QSize(176, 16))
        self.checkBox_afternoon_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.checkBox_afternoon_1, 1, 0, 1, 1)

        self.checkBox_afternoon_2 = QCheckBox(self.frame_4)
        self.checkBox_afternoon_2.setObjectName(u"checkBox_afternoon_2")
        self.checkBox_afternoon_2.setMinimumSize(QSize(176, 16))
        self.checkBox_afternoon_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.checkBox_afternoon_2, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"#pushButton_2{\n"
"	border:none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/res/icon/afternoon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon4)

        self.gridLayout_5.addWidget(self.pushButton_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(178, 60))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.checkBox_morning_2 = QCheckBox(self.frame_5)
        self.checkBox_morning_2.setObjectName(u"checkBox_morning_2")
        self.checkBox_morning_2.setMinimumSize(QSize(176, 16))
        self.checkBox_morning_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_morning_2.setTristate(False)

        self.gridLayout_6.addWidget(self.checkBox_morning_2, 2, 0, 1, 1)

        self.checkBox_morning_1 = QCheckBox(self.frame_5)
        self.checkBox_morning_1.setObjectName(u"checkBox_morning_1")
        self.checkBox_morning_1.setMinimumSize(QSize(176, 16))
        font2 = QFont()
        font2.setStrikeOut(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.checkBox_morning_1.setFont(font2)
        self.checkBox_morning_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_morning_1.setStyleSheet(u"")
        self.checkBox_morning_1.setChecked(False)

        self.gridLayout_6.addWidget(self.checkBox_morning_1, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"#pushButton{\n"
"	border:none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/res/icon/morning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon5)

        self.gridLayout_6.addWidget(self.pushButton, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 0, 180, 180))
        self.frame_11.setMinimumSize(QSize(180, 180))
        self.frame_11.setStyleSheet(u"#frame_11{\n"
"	border: 1px solid #00c8ff;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.frame_11)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(30, 49, 120, 120))
        self.frame_10.setMinimumSize(QSize(120, 120))
        self.frame_10.setMaximumSize(QSize(120, 120))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 3, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_10)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(25, 25))
        self.pushButton_13.setMaximumSize(QSize(25, 25))
        icon6 = QIcon()
        icon6.addFile(u":/res/icon/whatweather.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_13.setIcon(icon6)

        self.gridLayout_3.addWidget(self.pushButton_13, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_10)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(25, 25))
        self.pushButton_15.setMaximumSize(QSize(25, 25))
        icon7 = QIcon()
        icon7.addFile(u":/res/icon/windpower.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_15.setIcon(icon7)

        self.gridLayout_3.addWidget(self.pushButton_15, 3, 0, 1, 1)

        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_10)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(25, 25))
        self.pushButton_14.setMaximumSize(QSize(25, 25))
        icon8 = QIcon()
        icon8.addFile(u":/res/icon/temperature.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon8)

        self.gridLayout_3.addWidget(self.pushButton_14, 2, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_10)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(25, 25))
        self.pushButton_12.setMaximumSize(QSize(25, 25))
        icon9 = QIcon()
        icon9.addFile(u":/res/icon/city.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon9)

        self.gridLayout_3.addWidget(self.pushButton_12, 0, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_11)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(40, 10, 100, 40))
        self.pushButton_11.setMinimumSize(QSize(100, 40))
        self.pushButton_11.setMaximumSize(QSize(100, 40))
        icon10 = QIcon()
        icon10.addFile(u":/res/icon/shishitianqi.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon10)
        self.pushButton_11.setIconSize(QSize(411, 20))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.pushButton_16 = QPushButton(self.page_3)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(140, 162, 25, 25))
        self.pushButton_16.setStyleSheet(u"#pushButton_16:pressed{\n"
"	padding-left: 6px;\n"
"    padding-top: 6px;\n"
"    padding-right: 2px;\n"
"    padding-bottom: 2px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/res/icon/next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_16.setIcon(icon11)
        self.frame_12 = QFrame(self.page_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(10, 20, 152, 140))
        self.frame_12.setMinimumSize(QSize(152, 140))
        self.frame_12.setMaximumSize(QSize(152, 140))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_12)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_2.addWidget(self.label_12)

        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_2.addWidget(self.label_11)

        self.lineEdit = QLineEdit(self.frame_12)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 25))
        self.lineEdit.setStyleSheet(u"#lineEdit{\n"
"	border:none;\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.plainTextEdit = QPlainTextEdit(self.frame_12)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 50))
        self.plainTextEdit.setStyleSheet(u"#plainTextEdit{\n"
"	border:none;\n"
"}")

        self.verticalLayout_2.addWidget(self.plainTextEdit)

        self.pushButton_17 = QPushButton(self.page_3)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(100, 162, 25, 25))
        self.pushButton_17.setStyleSheet(u"#pushButton_16:pressed{\n"
"	padding-left: 6px;\n"
"    padding-top: 6px;\n"
"    padding-right: 2px;\n"
"    padding-bottom: 2px;\n"
"}\n"
"\n"
"QToolTip {\n"
"    background-color: #2e2e2e;\n"
"    color: white;\n"
"    border: 1px solid #aaa;\n"
"    padding: 6px;\n"
"    font-size: 13px;\n"
"    border-radius: 4px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/res/icon/translate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_17.setIcon(icon12)
        self.stackedWidget.addWidget(self.page_3)
        self.frame_6 = QFrame(self.frame_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 200, 230, 121))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(209, 60, 20, 16))
        self.pushButton_4.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_4.setStyleSheet(u"#pushButton_4{\n"
"	border:none;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/res/icon/jump.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon13)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 60, 56, 56))
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton_9 = QPushButton(self.frame_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(209, 80, 20, 16))
        self.pushButton_9.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_9.setStyleSheet(u"#pushButton_9{\n"
"	border:none;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/res/icon/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon14)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(9, 10, 220, 40))
        self.frame_8.setMinimumSize(QSize(180, 40))
        self.frame_8.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QToolTip {\n"
"    background-color: #2e2e2e;\n"
"    color: white;\n"
"    border: 1px solid #aaa;\n"
"    padding: 6px;\n"
"    font-size: 13px;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 25))
        self.label_2.setStyleSheet(u"#label_2{\n"
"	border:1px solid red;\n"
"	border-radius:10px;\n"
"	\n"
"	\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(50, 25))
        self.label_3.setStyleSheet(u"#label_3{\n"
"	border:1px solid blue;\n"
"	border-radius:10px;\n"
"	\n"
"	\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 25))
        self.label_4.setStyleSheet(u"#label_4{\n"
"	border:1px solid #ff95fd;\n"
"	border-radius:10px;\n"
"	\n"
"	\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.label_4)

        self.pushButton_10 = QPushButton(Form)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(121, -6, 25, 25))
        self.pushButton_10.setStyleSheet(u"#pushButton_10{\n"
"	border:none;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/res/icon/nail.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon15)

        self.retranslateUi(Form)
        self.pushButton_9.clicked.connect(Form.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u610f", None))
        self.checkBox_evening_1.setText("")
        self.checkBox_evening_2.setText("")
        self.pushButton_3.setText("")
        self.checkBox_afternoon_1.setText("")
        self.checkBox_afternoon_2.setText("")
        self.pushButton_2.setText("")
        self.checkBox_morning_2.setText("")
        self.checkBox_morning_1.setText("")
        self.pushButton.setText("")
        self.label_9.setText("")
        self.pushButton_13.setText("")
        self.label_5.setText("")
        self.pushButton_15.setText("")
        self.label_8.setText("")
        self.label_7.setText("")
        self.pushButton_14.setText("")
        self.pushButton_12.setText("")
        self.pushButton_11.setText("")
        self.pushButton_16.setText("")
        self.label_12.setText("")
        self.label_11.setText("")
        self.pushButton_17.setText("")
        self.pushButton_4.setText("")
        self.label.setText("")
        self.pushButton_9.setText("")
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.pushButton_10.setText("")
    # retranslateUi

