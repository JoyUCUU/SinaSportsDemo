import yaml
from appium import webdriver

from testAndroid.page.main import BasePage, Main


class App(BasePage):
    _package = "cn.com.sina.sports"
    _activity = ".app.MainActivity"

    def start(self):
        caps = {}
        deviceName = yaml.safe_load(open("../page/configuration.yaml"))['caps']['udid']
        print(type(deviceName))
        caps = {
            'platformName': 'Android',
            'deviceName': deviceName,
            'appPackage': 'cn.com.sina.sports',
            'appActivity': '.app.MainActivity',
            # 记住上一次的弹窗，登陆等的信息，不会重置
            # 'noReset': 'true',
            # 之前停留在那个页面仍在哪个页面继续
            # 'dontStopAppOnReset': 'True',
            'skipDeviceInitialization': 'true',
            # 因为输入搜索框的有中文
            'unicodeKeyBoard': 'true',
            'resetKeyBoard': 'true'
        }
        print(caps)
        self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self._driver.implicitly_wait(3)
        return self

    def main(self) -> Main():
        return Main(self._driver)
