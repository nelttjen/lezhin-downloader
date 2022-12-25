from PyQt5.QtGui import QFont


def get_font(size: int = 8):
    font = QFont()
    font.setPointSize(size)
    return font
