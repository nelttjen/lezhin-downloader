from PyQt5.QtWidgets import QDialog, QListWidget, QAbstractItemView
from .ui.ChaptersWindowUI import ChaptersWindowUI


class ChapterWindow(QDialog, ChaptersWindowUI):
    def __init__(self, parent, link):
        super().__init__(parent=parent)
        self.__parent = parent
        self.setup_window()

        self.link = link

        self.choose_chapters = []
        self.result_chapters = {
            'link': link,
            'content': []
        }

        self.get_chapters_to_choose()

    def setup_window(self):
        self.setFixedSize(ChaptersWindowUI.Meta.WINDOW_WIDTH, ChaptersWindowUI.Meta.WINDOW_HEIGHT)
        self.setWindowTitle(ChaptersWindowUI.Meta.WINDOW_TITLE)

        self.main_list = QListWidget(self)
        self.main_list.setGeometry(10, 55, self.Meta.WINDOW_WIDTH - 20, self.Meta.WINDOW_HEIGHT - 105)
        self.main_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.complete_choose.clicked.connect(self.complete_choosing)

    def get_chapters_to_choose(self):
        self.status_label.setText('Получение списка глав')
        self.__parent.driver.chapter_choose_create(self, self.link)

    def set_chapters_view(self):
        self.status_label.setText('Готово! Выберите главы ниже')
        for item in self.choose_chapters:
            table_item = f'{item["id"]} - {item["title"]} - is free: {item["is_free"]} - is purchased: {item["purchased"]}'
            self.main_list.addItem(table_item)
        self.complete_choose.setDisabled(False)

    def complete_choosing(self):
        items = self.main_list.selectedItems()
        for item in items:
            try:
                ch_id = int(item.text().split(' - ')[0])
            except ValueError:
                ch_id = item.text().split(' - ')[0]
            for ch_item in self.choose_chapters:
                if ch_item['id'] == ch_id:
                    self.result_chapters['content'].append(ch_item)
        self.accept()
