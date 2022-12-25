import sys

from app.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    code = app.exec_()
    sys.exit(code)