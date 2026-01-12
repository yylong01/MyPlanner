import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QSystemTrayIcon, QMenu, QMainWindow, QMessageBox, QListWidgetItem
)
from PySide6.QtGui import QIcon, QAction, QGuiApplication, QMovie
from ui.Ui_mainWin import Ui_MainWindow
from ui.Ui_task_win import Ui_Form
from PySide6.QtCore import QDate, Qt, QObject, QThread, Signal
from PySide6.QtWidgets import QInputDialog
from datetime import datetime
import os
import json
import rec_rc


from functions import (
    load_task_file, add_task, show_task_data, get_nearest_three_events_with_dates, 
    show_matter, get_weather, get_random_word
)


def resource_path(relative_path):
    """兼容打包后获取资源路径"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



# 多线程获取单词类
class WordWorker(QObject):
    finished = Signal(dict)

    def run(self):
        word_info = get_random_word()
        self.finished.emit(word_info)





# 后台窗口
class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # 设置无边框
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # 设置图标
        self.setWindowIcon(QIcon(resource_path("icon/winIcon.png")))

        
        



        # 信号

        # 页面跳转
        self.ui.pushButton_about.clicked.connect(self.show_about)
        self.ui.pushButton_list.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_settings.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(1))
        # 点击日历返回日期
        self.ui.calendarW.clicked.connect(self.clickCalendar)
        # 回到今天功能
        self.ui.pushButton_6.clicked.connect(self.toToday)

        # 添加任务
        self.ui.pushButton_3.clicked.connect(lambda: add_task(self, self.ui.comboBox.currentText()))

        # 修改任务
        self.ui.listWidget.itemDoubleClicked.connect(self.edit_task)

        # 回到task窗口
        self.ui.pushButton_2.clicked.connect(self.toTaksWin)

        # 加载未来事件
        self.ui.pushButton_load_event.clicked.connect(self.load_events)

        # 添加未来事件
        self.ui.pushButton_add_event.clicked.connect(self.add_event)

        self.ui.listWidget_events.itemDoubleClicked.connect(self.delete_event)



    # 槽函数

    # 显示关于窗口
    def show_about(self):
        QMessageBox.about(self, 
                          "About", 
                          "Author:YYL\nVersion 1.2")

    # 点击日历返回日期    
    def clickCalendar(self):
        selected_data = self.ui.calendarW.selectedDate()
        load_task_file(self, selected_data)
        

    # 回到今天功能
    def toToday(self):
        today = QDate.currentDate()
        self.ui.calendarW.setSelectedDate(today)
        load_task_file(self, today)
            


    # 双击修改任务
    # itemDoubleClicked 信号会自动把被双击的 QListWidgetItem 对象作为参数传递给槽函数，
    # 所以槽函数 edit_task 必须带一个参数来接收它。
    def edit_task(self, item):
        selected_date = self.ui.calendarW.selectedDate()
        date_str = selected_date.toString('yyyy-MM-dd')
        file_path = os.path.join("list", f"{date_str}.json")
        if not os.path.exists(file_path):
            return
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 找到被点击的item在listWidget中的索引
        row = self.ui.listWidget.row(item)

        # 根据 row 位置判断是上午、下午还是晚上，第几个任务
        period, index = None, None
        if row in [1, 2]:
            period = "上午"
            index = row - 1
        elif row in [4, 5]:
            period = "下午"
            index = row - 4
        elif row in [7, 8]:
            period = "晚上"
            index = row - 7

        if period is not None and index < len(data[period]):
            old_text = data[period][index]
            new_text, ok = QInputDialog.getText(self, "修改任务", f"修改 {period} 的任务：", text=old_text)
            if ok and new_text.strip():
                data[period][index] = new_text.strip()
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                # 更新显示
                show_task_data(self, data)

    def toTaksWin(self):
        self.close()
        self.taskWin = TaskWin()
        self.taskWin.show()
        self.taskWin.activateWindow()

    # 添加未来事件
    def add_event(self):
        name, ok1 = QInputDialog.getText(self, "添加事件", "请输入事件名称：")
        if not ok1 or not name.strip():
            return
        
        date_str, ok2 = QInputDialog.getText(self, "添加事件日期", "请输入事件日期(格式:YYYY-MM-DD):")
        if not ok2:
            return

        try:
            event_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            QMessageBox.warning(self, "错误", "日期格式错误，应为 YYYY-MM-DD")
            return

        file_path = resource_path("list/events.json")
        events = []
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                events = json.load(f)

        events.append({"name": name.strip(), "date": date_str})
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(events, f, ensure_ascii=False, indent=4)

        self.load_events()       


    # 显示未来事件
    def load_events(self):
        self.ui.listWidget_events.clear()  # 确保你有一个 listWidget_events 控件
        file_path = resource_path("list/events.json")
        if not os.path.exists(file_path):
            return
        with open(file_path, "r", encoding="utf-8") as f:
            events = json.load(f)

        today = datetime.today().date()

        for idx, event in enumerate(events):
            event_date = datetime.strptime(event["date"], "%Y-%m-%d").date()
            delta_days = (event_date - today).days
            display_text = f"{event['name']}（剩余 {delta_days} 天）"
            item = QListWidgetItem(display_text)
            item.setData(Qt.UserRole, idx)  # 记录索引用于删除
            self.ui.listWidget_events.addItem(item)

        # self.ui.listWidget_events.itemDoubleClicked.connect(self.delete_event)

    # 删除未来事件
    def delete_event(self, item):
        reply = QMessageBox.question(self, "删除事件", "确定要删除该事件吗？", 
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            index = item.data(Qt.UserRole)
            file_path = resource_path("list/events.json")
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    events = json.load(f)
                if 0 <= index < len(events):
                    events.pop(index)
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(events, f, ensure_ascii=False, indent=4)
                    self.load_events()






# 任务窗口
class TaskWin(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # 设置无边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window | Qt.WindowStaysOnTopHint)  # Qt.Tool 防止任务栏显示图标

        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # 设置图标
        self.setWindowIcon(QIcon(resource_path("icon/winIcon.png")))


        self.show()

        # 信号
        self.ui.pushButton_4.clicked.connect(self.toMainWin)

        # 移动窗口到右下角
        self.move_to_bottom_right()

        # 加载今日任务显示到复选框(checkbox)
        self.load_today_tasks()

        # 加载未来事件
        show_matter(self)

        # 创建 QMovie 对象
        movie = QMovie(resource_path("icon/dancing.gif"))
        movie.setScaledSize(self.ui.label.size())  # 自适应label大小
        self.ui.label.setMovie(movie)
        movie.start()

        self.mo = 0 # 控制小人动不动
        self.ui.label.mousePressEvent = self.danceYN

        # 跳转清单页
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        # 跳转天气页 
        self.ui.pushButton_6.clicked.connect(self.toPageWeather)

        # 跳转单词页
        self.ui.pushButton_7.clicked.connect(self.toPageWord)

        # 获取随即单词
        self.ui.pushButton_16.clicked.connect(self.getWord)





    
    # 函数

    # 窗口移动有下端
    def move_to_bottom_right(self):
        screen_geometry = QGuiApplication.primaryScreen().availableGeometry()
        x = screen_geometry.width() - self.width()
        y = screen_geometry.height() - self.height()
        self.move(x, y)

    # 去设置窗口
    def toMainWin(self):
        self.close()
        self.mainWin = MainWin()
        self.mainWin.show()

    # 加载任务
    def load_today_tasks(self):
        # 获取今天日期字符串
        today = QDate.currentDate()
        date_str = today.toString("yyyy-MM-dd")

        file_path = os.path.join("list", f"{date_str}.json")

        # 先清空所有复选框文字和状态
        for cb in [
            self.ui.checkBox_morning_1, self.ui.checkBox_morning_2,
            self.ui.checkBox_afternoon_1, self.ui.checkBox_afternoon_2,
            self.ui.checkBox_evening_1, self.ui.checkBox_evening_2,
        ]:
            cb.setText("")
            cb.setChecked(False)
            cb.setEnabled(False)  # 如果没有任务禁用checkbox

        if not os.path.exists(file_path):
            return  # 没有任务文件就返回

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 填充上午任务
        for i, task_text in enumerate(data.get("上午", [])):
            if i >= 2:
                break
            cb = getattr(self.ui, f"checkBox_morning_{i+1}")
            cb.setText(task_text)
            cb.setEnabled(True)

        # 填充下午任务
        for i, task_text in enumerate(data.get("下午", [])):
            if i >= 2:
                break
            cb = getattr(self.ui, f"checkBox_afternoon_{i+1}")
            cb.setText(task_text)
            cb.setEnabled(True)

        # 填充晚上任务
        for i, task_text in enumerate(data.get("晚上", [])):
            if i >= 2:
                break
            cb = getattr(self.ui, f"checkBox_evening_{i+1}")
            cb.setText(task_text)
            cb.setEnabled(True)

    # 小人跳舞否
    def danceYN(self, event):
        self.mo += 1
        if self.mo % 2 == 0:
            self.ui.label.movie().start()
        else:
            self.ui.label.movie().stop()

    # 跳转到天气页
    def toPageWeather(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        amap_key = "a312e471d3d4c7ec2e73baf1989fe74e"
        city_adcode = "130100"  # 石家庄的adcode

        weather = get_weather(self, city_adcode, amap_key)
        # print(weather)
        self.ui.label_5.setText(weather['城市'])
        self.ui.label_7.setText(weather['天气'])
        self.ui.label_8.setText(weather['温度'])
        self.ui.label_9.setText(weather['风力'])

    # 获取随机单词多线程
    def getWord(self):
        self.thread = QThread()
        self.worker = WordWorker()

        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.onWordReady)

        # 清理线程
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
    # 获取玩单词后通过此函数展示
    def onWordReady(self, word_info):
        self.ui.label_12.setText("word: " + word_info['word'])
        self.ui.label_11.setText("accent: " + word_info['accent'])
        self.ui.lineEdit.setText("mean: " + word_info['mean_cn'])
        self.ui.plainTextEdit.setPlainText("sentence: " + word_info['sentence'])
        self.ui.pushButton_17.setToolTip(word_info['sentence_trans'])



    # 跳转单词页
    def toPageWord(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        







# 托盘程序
class TrayApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # 初始化主窗口（不显示）
        self.win = TaskWin()
        self.win.hide()

        # 托盘图标
        self.tray = QSystemTrayIcon(QIcon(resource_path("icon/winIcon.png")))  
        self.tray.setToolTip("任务清单")  
        self.tray.show()

        # 托盘右键菜单
        self.menu = QMenu()
        action_show = QAction("显示主界面")
        action_exit = QAction("退出")

        self.menu.addAction(action_show)
        self.menu.addAction(action_exit)
        self.tray.setContextMenu(self.menu)

        # 菜单绑定
        action_show.triggered.connect(self.toggle_window)
        action_exit.triggered.connect(self.quit)

        # 双击托盘图标显示窗口
        self.tray.activated.connect(self.tray_clicked)

    def toggle_window(self):
        if self.win.isVisible():
            self.win.hide()
        else:
            self.win.show()
            self.win.activateWindow()

    def tray_clicked(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.toggle_window()
        
    






# if __name__ == "__main__":
#     app = QApplication([])
#     win = TaskWin()
#     win.show()
#     app.exec()        
if __name__ == "__main__":
    app = TrayApp(sys.argv)
    sys.exit(app.exec())







