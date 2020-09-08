import yaml
from selenium.webdriver.common.by import By

from testAndroid.page.BasePage import BasePage


class Main(BasePage):
    def goto_search(self):
        self.steps("../page/main.yaml")
