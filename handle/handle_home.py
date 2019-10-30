#操作层
import page


class HomeHandle(page.HomePage):
    #点击"我"元素
    def tap_me(self):
        self.execute_tap(self.get_me_ele())
