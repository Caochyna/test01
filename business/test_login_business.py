from selenium.webdriver.common.by import By

import handle
import base


class TestLogin:
    def setup(self):
        self.driver = base.get_driver()
        self.handle = handle.TotalHandle(self.driver)

    def test_login(self):
        # 首页点击我元素
        self.handle.init_home().tap_me()
        # 点击已有账号，去登陆元素
        self.handle.init_me().tap_to_login()
        # 输入用户名
        self.handle.init_login().input_account()
        # 输入密码
        self.handle.init_login().input_pwd()
        # 点击登陆按钮
        self.handle.init_login().tap_login_btn()
        # 断言toast框
        toast_feature = By.XPATH, "//*[contains(@text,'用户')]"
        ele = self.handle.init_login().get_element(toast_feature, 0.5)
        if ele.text == '此用户不存在':
            assert True
        else:
            assert False
