import handle


class TotalHandle:
    def __init__(self, driver):
        self.driver = driver

    def init_home(self):
        return handle.HomeHandle(self.driver)

    def init_me(self):
        return handle.MeHandle(self.driver)

    def init_login(self):
        return handle.LoginHandle(self.driver)
