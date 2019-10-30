import page


class LoginHandle(page.LoginPage):
    # 输入用户名
    def input_account(self):
        self.execute_input(self.get_account_ele(), "11111")

    # 输入密码
    def input_pwd(self):
        self.execute_input(self.get_pwd_ele(), "22222")

    # 点击登陆按钮
    def tap_login_btn(self):
        self.execute_tap(self.get_login_btn_ele())
