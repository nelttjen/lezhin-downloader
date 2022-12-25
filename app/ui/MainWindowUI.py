from PyQt5.QtWidgets import QLineEdit, QPushButton, QCheckBox, QLabel, QProgressBar
from PyQt5.QtCore import Qt
from ..utils.font import get_font


class MainWindowUI:

    class Meta:
        WINDOW_WIDTH = 800
        WINDOW_HEIGHT = 600
        WINDOW_TITLE = 'Lezhin downloader'
        THREAD_DOWNLOAD_FORMAT = 'Загружено: {}/{}, Загружается: Глава {}'

    def centralizate_width(self, width) -> int:
        return int(self.Meta.WINDOW_WIDTH / 2 - width / 2)

    def centralizate_height(self, height) -> int:
        return int(self.Meta.WINDOW_HEIGHT / 2 - height / 2)

    def set_ui_disabled(self, val: bool):
        self.main_line.setDisabled(val)
        self.main_button.setDisabled(val)

    def __init__(self):
        self.main_line = QLineEdit(self)
        self.main_line.setGeometry(self.centralizate_width(300), 25, 300, 30)
        self.main_line.setPlaceholderText('Ссылка на проект')

        self.main_button = QPushButton(self)
        self.main_button.setGeometry(self.centralizate_width(150), 60, 150, 40)
        self.main_button.setText('Выбрать главы')

        lab1 = QLabel(self)
        lab1.setText('Статус: ')
        lab1.setGeometry(5, self.Meta.WINDOW_HEIGHT - 50, lab1.width(), 50)
        lab1.setFont(get_font(14))

        self.status_label = QLabel(self)
        self.status_label.setText('Инициализация...')
        self.status_label.setGeometry(lab1.width(), self.Meta.WINDOW_HEIGHT - 50, 350, 50)
        self.status_label.setFont(get_font(14))

        lab2 = QLabel(self)
        lab2.setText('Статус загрузки:')
        lab2.setGeometry(self.centralizate_width(300), 200, 300, 50)
        lab2.setFont(get_font(13))
        lab2.setAlignment(Qt.AlignCenter)

        self.download_status_label = QLabel(self)
        self.download_status_label.setText('Выбрано 0 глав')
        self.download_status_label.setGeometry(self.centralizate_width(300), 250, 300, 50)
        self.download_status_label.setFont(get_font(13))
        self.download_status_label.setAlignment(Qt.AlignCenter)

        self.download_button = QPushButton(self)
        self.download_button.setText('Загрузить')
        self.download_button.setFont(get_font(13))
        self.download_button.setGeometry(self.centralizate_width(150), 300, 150, 50)
        self.download_button.setDisabled(True)

        self.download_status_thread = QLabel(self)
        self.download_status_thread.setText(self.Meta.THREAD_DOWNLOAD_FORMAT.format(0, 0, '-'))
        self.download_status_thread.setGeometry(self.centralizate_width(400), 425, 400, 50)
        self.download_status_thread.setFont(get_font(12))
        self.download_status_thread.setAlignment(Qt.AlignCenter)

        self.set_ui_disabled(True)