import json
import time

from PyQt5.QtCore import QThread
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from .threads.LoginThread import LoginThread
from .threads.ChapterThread import ChapterThread
from .threads.DownloadQueueThread import DownloadQueueThread
from config import DEBUG
from app.ui.MainWindowUI import MainWindowUI


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
        worker = LoginThread(self.parent, self.driver, self.username, self.password)
        worker.start()

    def chapter_choose_create(self, bind_to, link):
        thread = ChapterThread(bind_to, self.driver, link)
        thread.start()

    def start_download(self, to_download, fake=None):
        thread = DownloadQueueThread(self.parent, self.driver, to_download, fake=fake)
        thread.val_signal.connect(self.val_answer)
        thread.done.connect(self.done)
        thread.start()

    def val_answer(self, val):
        if self.parent.download_bar.maximum() != val[1]:
            self.parent.download_bar.setMaximum(val[1])
            self.parent.download_bar.setValue(1)
        else:
            self.parent.download_bar.setValue(val[0])
        self.parent.download_status_thread.setText(MainWindowUI.Meta.THREAD_DOWNLOAD_FORMAT.format(*val))

    def done(self):
        self.parent.download_bar.setValue(0)
        self.parent.download_status_thread.setText('Загрузка завершена')