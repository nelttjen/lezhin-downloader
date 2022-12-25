from PyQt5.QtCore import QObject
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class LoginThread(QObject):

    def __init__(self, parent, driver: Chrome, username, password):
        super().__init__(parent)
        self.driver = driver
        self.username = username
        self.password = password
        self.__parent = parent

    def run(self) -> None:
        self.driver.get('https://www.lezhin.com/ko/login/')
        self.driver.find_element(By.CSS_SELECTOR, '#login-email').send_keys(self.username)
        self.driver.find_element(By.CSS_SELECTOR, '#login-password').send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, 'form.account > div > button').click()
        self.__parent.login_done()