# 定位首页元素
from selenium.webdriver.common.by import By

import base


class HomePage(base.BaseAction):
    # "我"元素
    me_feature = By.ID, "com.yunmall.lc:id/tab_me"

    def get_me_ele(self):
        return self.get_element(self.me_feature, 1)
