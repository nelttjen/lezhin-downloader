from PyQt5.QtWidgets import QListWidget, QPushButton, QLabel
from ..utils.font import get_font


class ChaptersWindowUI:

    class Meta:
        WINDOW_WIDTH = 800
        WINDOW_HEIGHT = 600
        WINDOW_TITLE = 'Выбор чаптеров'

    def __init__(self):
        lab1 = QLabel(self)
        lab1.setText('Статус: ')
        lab1.setGeometry(5, 5, lab1.width(), 50)
        lab1.setFont(get_font(14))

        self.status_label = QLabel(self)
        self.status_label.setText('Инициализация...')
        self.status_label.setGeometry(lab1.width(), 5, 350, 50)
        self.status_label.setFont(get_font(14))

        self.complete_choose = QPushButton(self)
        self.complete_choose.setGeometry(5, self.Meta.WINDOW_HEIGHT - 45, self.Meta.WINDOW_WIDTH - 10, 40)
        self.complete_choose.setText('Выбрать')
        self.complete_choose.setDisabled(True)