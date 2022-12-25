from PyQt5.QtWidgets import QMainWindow
from driver.ChromeDriver import ChromeDriver

from .ui.MainWindowUI import MainWindowUI
from .utils.show_messages import show_info


class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self):
        super().__init__()
        self.driver = ChromeDriver(self)
        self.driver.login()

        self.setup_window()

    def setup_window(self):
        self.setFixedSize(MainWindowUI.Meta.WINDOW_WIDTH, MainWindowUI.Meta.WINDOW_HEIGHT)
        self.setWindowTitle(MainWindowUI.Meta.WINDOW_TITLE)

    def login_done(self):
        try:
            show_info(self, 'Логин завершен')
        except:
            pass