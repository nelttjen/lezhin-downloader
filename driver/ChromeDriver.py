import json
import time

from PyQt5.QtCore import QThread
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from .threads.LoginThread import LoginThread


class ChromeDriver:
    def __init__(self, parent):
        with open('settings.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.driver = Chrome(data.get('driver_path'))
        self.setup_driver()
        self.username = data.get('username')
        self.password = data.get('password')
        self.parent = parent

    def setup_driver(self):
        self.driver.set_window_rect(0, 0, 500, 700)

    def login(self):
        thread = QThread(self.parent)
        worker = LoginThread(self.parent, self.driver, self.username, self.password)
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        thread.start()

    def chapter_choose_create(self):
        pass
