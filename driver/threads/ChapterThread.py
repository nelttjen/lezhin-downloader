from PyQt5.QtCore import QThread
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from app.utils.clear_int import get_clear_int


class ChapterThread(QThread):

    def __init__(self, parent, driver: Chrome, link):
        super().__init__(parent)
        self.driver = driver
        self.link = link

        self.__parent = parent

    def run(self) -> None:
        result = []
        self.driver.get(self.link)
        try:
            items = self.driver.find_elements(By.CSS_SELECTOR, '.episode__button')
        except:
            self.__parent.status_label.setText('Не удалось получить список глав :(')
            return

        prologue_count = 1

        for item in items:
            curr_item = {}
            try:
                curr_item['episode_type'] = item.get_attribute('data-episode-type')
                curr_item['is_free'] = item.get_attribute('data-free')
                curr_item['purchased'] = item.get_attribute('data-purchased')
                clear_id = get_clear_int(item.find_element(By.CSS_SELECTOR, '.episode__name').text)
                if clear_id and item.get_attribute('data-episode-type') == 'g':
                    curr_item['id'] = int(clear_id)
                else:
                    if item.get_attribute('data-episode-type') == 'p':
                        curr_item['id'] = f'p{prologue_count}'
                        prologue_count += 1
                    else:
                        continue
                curr_item['title'] = item.find_element(By.CSS_SELECTOR, '.episode__title').text
                curr_item['date'] = item.find_element(By.CSS_SELECTOR, '.episode__freeDate').text
                result.append(curr_item)
            except:
                continue

        self.__parent.choose_chapters = result
        self.__parent.set_chapters_view()
