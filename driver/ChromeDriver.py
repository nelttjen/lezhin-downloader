import json
import time

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
        thread = LoginThread(self.parent, self.driver, self.username, self.password)
        thread.start()