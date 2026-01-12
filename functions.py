from PySide6.QtCore import QDate
import os
import sys
import json
import random
from datetime import datetime
import requests
from PySide6.QtWidgets import QMessageBox, QInputDialog


def resource_path(relative_path):
    """兼容打包后获取资源路径"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



# 判断某个日期是否有任务，有则加载，没有则创建空任务
def load_task_file(self, date: QDate):
    
    folder = "list"
    if not os.path.exists(folder):
        os.makedirs(folder)

    date_str = date.toString('yyyy-MM-dd')
    file_path = os.path.join(folder, f"{date_str}.json")

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                show_task_data(self, data)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {

            "上午": [],
            "下午": [],
            "晚上": []
        }
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            # print("创建成功")
        show_task_data(self, data)
    

# 任务添加
def add_task(self, period: str):
    selected_date = self.ui.calendarW.selectedDate()
    date_str = selected_date.toString('yyyy-MM-dd')
    file_path = os.path.join("list", f"{date_str}.json")

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {"上午": [], "下午": [], "晚上": []}

    if len(data[period]) >= 2:
        QMessageBox.warning(self, "提示", f"{period}最多只能添加2个任务！")
        return

    task_text, ok = QInputDialog.getText(self, "添加任务", f"请输入{period}任务内容：")
    if ok and task_text.strip():
        data[period].append(task_text.strip())

        # 写到json文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        show_task_data(self, data)



# 显示任务
def show_task_data(self, data):
    item1 = self.ui.listWidget.item(1)
    item1.setText("")
    item2 = self.ui.listWidget.item(2) 
    item2.setText("")

    item3 = self.ui.listWidget.item(4)
    item3.setText("")
    item4 = self.ui.listWidget.item(5)
    item4.setText("")

    item5 = self.ui.listWidget.item(7)
    item5.setText("")
    item6 = self.ui.listWidget.item(8)
    item6.setText("")

    if len(data['上午']) > 0:
        item1.setText(data['上午'][0])
    if len(data['上午']) > 1:
        item2.setText(data['上午'][1]) 
    if len(data['下午']) > 0:
        item3.setText(data['下午'][0]) 
    if len(data['下午']) > 1:
        item4.setText(data['下午'][1]) 
    if len(data['晚上']) > 0:
        item5.setText(data['晚上'][0]) 
    if len(data['晚上']) > 1:
        item6.setText(data['晚上'][1]) 



# 获取未来最近三个事件
'''
    # 目标输出格式:
    [
        {"name": "考试", "date": "2025-06-30"},
        {"name": "朋友聚会", "date": "2025-07-01"},
        {"name": "旅游", "date": "2025-07-10"}
    ]
'''
def get_nearest_three_events_with_dates():
    file_path = resource_path("list/events.json")
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        events = json.load(f)

    today = datetime.today().date()

    # 过滤未来事件
    future_events = [
        event for event in events
        if datetime.strptime(event["date"], "%Y-%m-%d").date() > today
    ]

    # 按日期升序排序
    future_events.sort(key=lambda e: datetime.strptime(e["date"], "%Y-%m-%d"))

    # 返回前三个事件（包含 name 和 date）
    return future_events[:3]

# 显示最近三个事件
def show_matter(self):
    fMatter = get_nearest_three_events_with_dates()
    # print(fMatter)
    event_day = []
    event_name = []
    for item in fMatter:

    
        event_day.append(item["date"][5:])
        event_name.append(item["name"])

    self.ui.label_2.setText(event_day[0] if len(event_day) > 0 else "")
    self.ui.label_2.setToolTip(event_name[0] if len(event_name) > 0 else "")
    self.ui.label_3.setText(event_day[1] if len(event_day) > 1 else "")
    self.ui.label_3.setToolTip(event_name[1] if len(event_name) > 1 else "")
    self.ui.label_4.setText(event_day[2] if len(event_day) > 2 else "")
    self.ui.label_4.setToolTip(event_name[2] if len(event_name) > 2 else "")
    
# 获取天气信息
def get_weather(self, city_adcode, amap_key):
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    params = {
        "key": amap_key,
        "city": city_adcode,
        "extensions": "base",  # "base" 为实时天气，"all" 为预报
        "output": "JSON"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") == "1":
        weather_info = data["lives"][0]
        return {
            "城市": weather_info["city"],
            "天气": weather_info["weather"],
            "温度": weather_info["temperature"] + "°C",
            "风向": weather_info["winddirection"],
            "风力": weather_info["windpower"] + "级",
            "湿度": weather_info["humidity"] + "%",
            "更新时间": weather_info["reporttime"]
        }
    else:
        QMessageBox.warning(self, "天气查询失败", "出现错误")
        raise Exception("查询失败：" + data.get("info", "未知错误"))


# 随机读取单词
def get_random_word():
    # 文件夹路径
    folder_path = resource_path("word/words/")
    # 获取所有 json 文件名（确保是文件）
    file_list = [f for f in os.listdir(folder_path) if f.endswith(".json") and os.path.isfile(os.path.join(folder_path, f))]
    # 随机选择一个文件名
    random_file = random.choice(file_list)
    # 构建完整路径
    file_path = os.path.join(folder_path, random_file)
    # 读取 JSON 文件内容
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data

