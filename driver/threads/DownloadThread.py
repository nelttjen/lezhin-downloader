import os
import shutil

from PyQt5.QtCore import QObject, pyqtSignal
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from app.ui.MainWindowUI import MainWindowUI

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}


class DownloadThread(QObject):

    val_signal = pyqtSignal(list)

    def __init__(self, parent, link, save_to, session, total_download, chapter_id, image_number):
        super().__init__()
        self.link = link
        self.session = session
        self.save_to = save_to
        self.__parent = parent
        self.total_download = total_download
        self.chapter_id = chapter_id
        self.image_number = image_number

    def get_response(self):
        return self.session.get(self.link)

    def run(self):
        count = 0
        response = None
        while count < 3:
            try:
                response = self.get_response()
                break
            except:
                count += 1

        if response:
            try:
                with open(self.save_to + f'/{self.image_number}.webp', 'wb') as outp:
                    outp.write(response.content)
            except:
                with open(self.save_to + f'/{self.image_number}.webp' + '.error', 'wb'):
                    ...
        else:
            with open(self.save_to + f'/{self.image_number}.webp' + '.error', 'wb'):
                ...
        try:
            val = self.__parent.download_bar.value()
            val += 1
            self.val_signal.emit([val, self.total_download - 1, self.chapter_id])
            # self.__parent.download_bar.setValue(val)
            # self.__parent.download_status_thread.setText(MainWindowUI.Meta.THREAD_DOWNLOAD_FORMAT.format(
            #     val, self.total_download, self.chapter_id
            # ))
        except:
            ...