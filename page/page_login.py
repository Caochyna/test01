from selenium.webdriver.common.by import By
import base


class LoginPage(base.BaseAction):
    # 用户名元素
    account_feature = By.ID, "com.yunmall.lc:id/logon_account_textview"

    # 密码元素
    pwd_feature = By.ID, "com.yunmall.lc:id/logon_password_textview"

    # 登陆按钮
    login_btn_feature = By.ID, "com.yunmall.lc:id/logon_button"

    def get_account_ele(self):
        return self.get_element(self.account_feature,1)

    def get_pwd_ele(self):
        return self.get_element(self.pwd_feature,1)

    def get_login_btn_ele(self):
        return self.get_element(self.login_btn_feature,1)
