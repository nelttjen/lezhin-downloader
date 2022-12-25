import logging

from PyQt5.QtWidgets import QMainWindow, QListWidget, QProgressBar, QWidget

from config import DEBUG
from driver.ChromeDriver import ChromeDriver

from .ui.MainWindowUI import MainWindowUI
from .ChaptersWindow import ChapterWindow
from .utils.show_messages import show_info, show_warn


class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self):
        super().__init__()
        self.driver = ChromeDriver(self)

        if not DEBUG:
            self.driver.login()
        else:
            self.login_done()

        self.setup_window()
        self.connect_buttons()

        self.to_download = {}

    def setup_window(self):
        self.setFixedSize(MainWindowUI.Meta.WINDOW_WIDTH, MainWindowUI.Meta.WINDOW_HEIGHT)
        self.setWindowTitle(MainWindowUI.Meta.WINDOW_TITLE)

        self.download_bar = QProgressBar(self)
        self.download_bar.setGeometry(self.centralizate_width(500) + 25, 375, 500, 30)
        self.download_bar.setValue(0)
        self.download_bar.setMaximum(100)

    def connect_buttons(self):
        self.main_button.clicked.connect(self.choose_chapters)
        self.download_button.clicked.connect(self.download_start)

    def choose_chapters(self):
        logging.info('here')
        link = self.main_line.text()
        if (link and link.startswith('https://www.lezhin.com')) or DEBUG:
            dialog = ChapterWindow(self, link)
            dialog.show()
            dialog.exec_()
            result = dialog.result_chapters
            self.download_status_label.setText(f'Выбрано {len(result["content"])} глав')
            self.to_download = result
            self.download_button.setDisabled(False)

        else:
            show_info(self, 'Введите валидную ссылку на тайтл')

    def login_done(self):
        try:
            # show_info(self, 'Логин завершен')
            self.status_label.setText('Логин завершен')
            self.set_ui_disabled(False)
        except:
            pass

    def download_start(self):
        self.driver.start_download(self.to_download)