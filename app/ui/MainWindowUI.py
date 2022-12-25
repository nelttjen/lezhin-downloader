from PyQt5.QtWidgets import QLineEdit, QPushButton, QCheckBox


class MainWindowUI:

    class Meta:
        WINDOW_WIDTH = 800
        WINDOW_HEIGHT = 600
        WINDOW_TITLE = 'Lezhin downloader'

    def centralizate_width(self, width) -> int:
        return int(self.Meta.WINDOW_WIDTH / 2 - width / 2)

    def centralizate_height(self, height) -> int:
        return int(self.Meta.WINDOW_HEIGHT / 2 - height / 2)

    def __init__(self):
        self.main_line = QLineEdit(self)
        self.main_line.setGeometry(self.centralizate_width(300), 25, 300, 30)