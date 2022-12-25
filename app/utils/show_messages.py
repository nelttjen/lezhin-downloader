from PyQt5.QtWidgets import QMessageBox


def show_info(parent, message, title='Информация'):
    QMessageBox.information(parent, title, message, QMessageBox.Ok)


def show_warn(parent, message, title='Предупреждение'):
    QMessageBox.warning(parent, title, message, QMessageBox.Ok)


def show_error(parent, message, title='Ошибка'):
    QMessageBox.critical(parent, title, message, QMessageBox.Ok)
