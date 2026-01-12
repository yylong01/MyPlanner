from PySide6.QtWidgets import (
    QApplication, QSystemTrayIcon, QMenu, QWidget, QMainWindow
)
from PySide6.QtGui import QIcon, QAction
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("托盘程序示例")
        self.setFixedSize(300, 200)

        # 系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("icon/night.png"))  # 换成你自己的图标路径
        self.tray_icon.setToolTip("点击图标可恢复窗口")

        # 托盘图标菜单
        menu = QMenu()
        restore_action = QAction("显示窗口")
        quit_action = QAction("退出")

        restore_action.triggered.connect(self.show_window)
        quit_action.triggered.connect(QApplication.quit)

        menu.addAction(restore_action)
        menu.addAction(quit_action)

        self.tray_icon.setContextMenu(menu)
        self.tray_icon.show()

        # 双击图标时恢复窗口
        self.tray_icon.activated.connect(self.on_tray_icon_activated)

        # 启动时隐藏窗口
        self.hide()

    def show_window(self):
        self.showNormal()
        self.activateWindow()

    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_window()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
