from PyQt5.QtWidgets import QDialog

from .ui.ChaptersWindowUI import ChaptersWindowUI


class ChapterWindow(QDialog, ChaptersWindowUI):
    def __init__(self, parent, link):
        super().__init__(parent=parent)
        self.__parent = parent
        self.setup_window()

    def setup_window(self):
        self.setFixedSize(ChaptersWindowUI.Meta.WINDOW_WIDTH, ChaptersWindowUI.Meta.WINDOW_HEIGHT)
        self.setWindowTitle(ChaptersWindowUI.Meta.WINDOW_TITLE)

