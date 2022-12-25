import sys

from app.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication


def init_logger():
    import logging
    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger()
    logger_handler = logging.StreamHandler()
    logger.addHandler(logger_handler)
    logger.removeHandler(logger.handlers[0])

    formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(name)s: %(message)s")
    logger_handler.setFormatter(formatter)


if __name__ == '__main__':
    init_logger()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    code = app.exec_()
    sys.exit(code)