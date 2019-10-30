from selenium.webdriver.common.by import By

import base


class MePage(base.BaseAction):
    # 已有账号，去登陆
    login_link_feature = By.ID, "com.yunmall.lc:id/gotologon"

    def get_login_link_ele(self):
        return self.get_element(self.login_link_feature,1)
