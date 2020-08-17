import pytest
from appium import webdriver
import time

chaohauele = "超话"
sendKey = "易建联"


class TestSinaSports:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'cn.com.sina.sports',
            'appActivity': '.app.MainActivity',
            # 记住上一次的弹窗，登陆等的信息，不会重置
            'noReset': 'true',
            # 之前停留在那个页面仍在哪个页面继续
            # 'dontStopAppOnReset': 'True',
            'skipDeviceInitialization': 'true',
            # 因为输入搜索框的有中文
            'unicodeKeyBoard': 'true',
            'resetKeyBoard': 'true'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        """
        1、打开新浪体育app
        2、点击搜索框
        3、搜索易建联
        4、查看并判断是否有易建联的超话
        :return:
        """
        # 获取搜索框元素
        search_ele = self.driver.find_element_by_xpath(
            "//android.widget.FrameLayout[@resource-id='cn.com.sina.sports:id/ll_search']")
        # 搜索框是否可用
        search_enabled = search_ele.is_enabled()
        print(f"search_enabled{search_enabled}")
        search_ele.click()
        self.driver.implicitly_wait(5)
        input_ele = self.driver.find_element_by_xpath(
            "//android.widget.EditText[@resource-id='cn.com.sina.sports:id/et_search_input']").send_keys(sendKey)
        self.driver.press_keycode(66)
        time.sleep(8)
        # 判断是否存在超话这个模块，
        isexist_chaohua = self.findItem(chaohauele)

    def findItem(self, el):
        source = self.driver.page_source
        if el in source:
            print(f"搜索结果中有{el}的超话")
            return True
        else:
            print(f"搜索结果中没有{el}的超话")
            return False


if __name__ == '__main__':
    pytest.main()
