import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    # 1工具方法之获取元素
    def get_element(self, feature, interval):

        wait = WebDriverWait(self.driver, 5, interval)
        try:
            obj = wait.until(lambda x: x.find_element(*feature))
        except Exception:
            # 代码如果能执行到这里，就说明目标元素不存在
            return None
        else:
            return obj

    def get_elements(self, feature):

        wait = WebDriverWait(self.driver, 5, 1)
        try:
            obj = wait.until(lambda x: x.find_elements(*feature))
        except Exception:
            # 代码如果能执行到这里，就说明目标元素不存在
            return None
        else:
            return obj

    def execute_tap(self, feature):
        action = TouchAction(self.driver)

        # 1 判断用户给定的数据类型
        if isinstance(feature, tuple):
            feature = self.get_element(feature)

        action.tap(feature).perform()

    # 2工具方法之获取屏幕大小
    def get_size(self):
        obj_size = self.driver.get_window_size()  # 此时返回的是字典 width height
        w = obj_size["width"]
        h = obj_size["height"]
        return w, h

    # 3工具方法之向左滑动
    def swipe_left(self, n):
        obj = self.get_size()
        for i in range(n):
            time.sleep(0.5)
            self.driver.swipe(obj[0] * 0.9, obj[1] * 0.5, obj[0] * 0.1, obj[1] * 0.5)

    # 4 工具方法之向上滑动
    def swipe_top(self, n, tm=1500):
        obj = self.get_size()
        for i in range(n):
            time.sleep(0.5)
            self.driver.swipe(obj[0] * 0.5, obj[1] * 0.9, obj[0] * 0.5, obj[1] * 0.1, tm)

    # 5 工具方法之递归查找元素
    def get_ele_recursion(self, feature):

        # 上来就去找元素，如果元素找到了，则直接返回元素
        # 如果元素没有找到，没有惯性的滑一屏， 再接着去找。如果找到了则返回元素
        obj = self.get_element(feature)

        if obj:
            return obj
        else:
            self.swipe_top(1, tm=4000)
            return self.get_ele_recursion(feature)

    def get_ele_ancestry(self, ancestry, sub):
        obj = self.get_element(ancestry)
        wait = WebDriverWait(obj, 5, 1)
        try:
            ele = wait.until(lambda x: x.find_element(*sub))
        except Exception:
            return None
        else:
            return ele

    # 输入方法
    def execute_input(self, feature, val):
        if isinstance(feature, tuple):
            feature = self.get_element(feature)

        feature.send_keys(val)
