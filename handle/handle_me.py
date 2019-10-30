# 操作层
import page


class MeHandle(page.MePage):
    # 点击已有账号，去登陆元素
    def tap_to_login(self):
        self.execute_tap(self.get_login_link_ele())
