from selenium.webdriver.common.by import By

from testAndroid.page.BasePage import BasePage


class Main(BasePage):
    def goto_search(self):
        self.find(By.ID, 'll_search').click()
