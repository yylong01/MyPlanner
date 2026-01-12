# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWin.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QGridLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTabWidget, QWidget)
import rec_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(929, 672)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#frame{\n"
"	border: 2px solid black;\n"
"}")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 129, 800, 484))
        self.frame.setStyleSheet(u"background-color: rgb(236, 225, 255);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(2, 2, 796, 31))
        self.frame_2.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(4, 0, 111, 31))
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(738, 1, 28, 28))
        self.pushButton.setStyleSheet(u"#pushButton{\n"
"	border:none;\n"
"}\n"
"\n"
"#pushButton:hover{\n"
"	padding-left: 3px;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/res/icon/min.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(768, 1, 28, 28))
        self.pushButton_2.setStyleSheet(u"#pushButton_2{\n"
"	border:none;\n"
"}\n"
"\n"
"#pushButton_2:hover{\n"
"	padding-left: 3px;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/res/icon/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(82, 36, 711, 441))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.calendarW = QCalendarWidget(self.page)
        self.calendarW.setObjectName(u"calendarW")
        self.calendarW.setGeometry(QRect(10, 0, 261, 251))
        self.calendarW.setStyleSheet(u"QCalendarWidget  QAbstractItemView {\n"
"    border: 1px solid blue;\n"
"	border-radius:5px;\n"
"}")
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(290, 10, 410, 240))
        self.frame_3.setMinimumSize(QSize(410, 240))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.listWidget = QListWidget(self.frame_3)
        icon2 = QIcon()
        icon2.addFile(u":/res/icon/morning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.NoBrush)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem.setBackground(brush);
        __qlistwidgetitem.setIcon(icon2);
        font = QFont()
        font.setBold(True)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setFont(font);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setFont(font);
        icon3 = QIcon()
        icon3.addFile(u":/res/icon/afternoon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3.setIcon(icon3);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem4.setFont(font);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem5.setFont(font);
        icon4 = QIcon()
        icon4.addFile(u":/res/icon/night.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        font1 = QFont()
        font1.setBold(False)
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem6.setFont(font1);
        __qlistwidgetitem6.setIcon(icon4);
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem7.setFont(font);
        __qlistwidgetitem8 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem8.setFont(font);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 10, 391, 221))
        self.listWidget.setStyleSheet(u"#listWidget{\n"
"	border: 1px solid black;\n"
"	border-radius:5px;\n"
"}")
        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(350, 270, 257, 43))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(350, 320, 257, 43))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 0, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_2.addWidget(self.pushButton_8, 0, 2, 1, 1)

        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 280, 321, 71))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 311, 51))
        self.label_4.setPixmap(QPixmap(u":/res/icon/welcome.png"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.tabWidget = QTabWidget(self.page_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 20, 621, 371))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.listWidget_events = QListWidget(self.tab)
        self.listWidget_events.setObjectName(u"listWidget_events")
        self.listWidget_events.setGeometry(QRect(30, 20, 256, 301))
        self.listWidget_events.setStyleSheet(u"QListWidget{\n"
"	border: 1px solid black;\n"
"	border-radius:5px;\n"
"}")
        self.pushButton_add_event = QPushButton(self.tab)
        self.pushButton_add_event.setObjectName(u"pushButton_add_event")
        self.pushButton_add_event.setGeometry(QRect(340, 80, 75, 23))
        self.pushButton_load_event = QPushButton(self.tab)
        self.pushButton_load_event.setObjectName(u"pushButton_load_event")
        self.pushButton_load_event.setGeometry(QRect(340, 40, 75, 23))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton_list = QPushButton(self.frame)
        self.pushButton_list.setObjectName(u"pushButton_list")
        self.pushButton_list.setGeometry(QRect(2, 32, 85, 45))
        font2 = QFont()
        font2.setPointSize(10)
        self.pushButton_list.setFont(font2)
        self.pushButton_settings = QPushButton(self.frame)
        self.pushButton_settings.setObjectName(u"pushButton_settings")
        self.pushButton_settings.setGeometry(QRect(2, 77, 85, 45))
        self.pushButton_settings.setFont(font2)
        self.pushButton_about = QPushButton(self.frame)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setGeometry(QRect(2, 122, 85, 45))
        self.pushButton_about.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.showMinimized)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"todo\u6e05\u5355-V1.0", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u5348", None));
        ___qlistwidgetitem1 = self.listWidget.item(3)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u5348", None));
        ___qlistwidgetitem2 = self.listWidget.item(6)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u665a\u4e0a", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e0a\u5348", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e0b\u5348", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u665a\u4e0a", None))

        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u56de\u5230\u4eca\u5929", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u5f00\u53d1", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u5f00\u53d1", None))
        self.label_4.setText("")
        self.pushButton_add_event.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u4e8b\u4ef6", None))
        self.pushButton_load_event.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u4e8b\u4ef6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5012\u8ba1\u65f6\u8bbe\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u5f85\u5f00\u53d1", None))
        self.pushButton_list.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u5355", None))
        self.pushButton_settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.pushButton_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

