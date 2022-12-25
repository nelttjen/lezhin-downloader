import logging
import os
import shutil

from PyQt5.QtCore import QThread, QObject, pyqtSignal
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from requests import Session

from config import settings
from .DownloadThread import DownloadThread

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}


class DownloadQueueThread(QThread):

    val_signal = pyqtSignal(list)
    done = pyqtSignal(bool)

    def __init__(self, parent, driver: Chrome, download_content, fake=None):
        super().__init__(parent=fake or parent)
        self.__parent = parent
        self.driver = driver
        self.download_content = download_content
        self.session = Session()

        self.threads = []

    def run(self) -> None:
        link: str = self.download_content.get('link')
        if link.endswith('/'):
            link = link[:-1]
        try:
            _dir = link.split('/')[-1]
            downl_dir = settings.get("save_path", '')
            if downl_dir.endswith('/'):
                downl_dir = downl_dir[:-1]
            if downl_dir and not os.path.isdir(downl_dir):
                os.mkdir(downl_dir)
            make_dir = downl_dir + '/' if downl_dir else ''
            os.mkdir(make_dir + _dir) if not os.path.isdir(make_dir + _dir) else None
            full_download_dir = make_dir + _dir
        except:
            logging.error('Не скачалось')
            self.__parent.download_status_label.setText('Ошибка в создании папки')
            return
        for download_item in self.download_content.get('content'):
            curr_link = link + "/" + str(download_item.get('id'))
            self.driver.get(curr_link)
            QThread.msleep(settings.get('load_page_delay', 5000))
            items = [item for item in self.driver.find_elements(By.CSS_SELECTOR, '.viewer-list > div.cut') if
                     'cutLicense' not in item.get_attribute('class')]
            total = len(items)
            if total == 0:
                continue
            ActionChains(self.driver).move_to_element(items[1]).perform()
            QThread.msleep(1000)
            imgs = self.driver.find_elements(By.CSS_SELECTOR, '.cut > img')
            img_url = None
            for img in imgs:
                if 'comics' in img.get_attribute('src'):
                    img_url = img.get_attribute('src')
            if not img_url:
                continue
            img_url1, img_url2 = img_url.split('.webp')
            img_url1 = '/'.join(img_url1.split('/')[:-1])
            img_url = img_url1 + '/{}.webp' + img_url2

            save_to = full_download_dir + '/' + str(download_item.get('id'))
            if os.path.isdir(save_to):
                shutil.rmtree(save_to)
            os.mkdir(save_to)

            for i in range(1, total):
                QThread.msleep(200)
                image_link = img_url.format(i)
                thread = QThread()
                worker = DownloadThread(self.__parent, image_link, save_to, self.session, total,
                                        download_item.get('id'), i)
                worker.moveToThread(thread)
                worker.val_signal.connect(self.val_signal_answer)
                thread.started.connect(worker.run)
                thread.start()
                self.threads.append((thread, worker))
            QThread.msleep(settings.get('switch_page_delay', 5000))
        self.done.emit(True)

    def val_signal_answer(self, val):
        self.val_signal.emit(val)