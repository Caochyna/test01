from appium import webdriver


def get_driver():

    desired_caps = dict()

    desired_caps["platformName"] = "Android"
    desired_caps["platformVersion"] = "5"
    desired_caps["deviceName"] = "emulator-5554"
    desired_caps["appPackage"] = "com.yunmall.lc"
    desired_caps["appActivity"] = "com.yunmall.ymctoc.ui.activity.MainActivity"
    desired_caps['noReset'] = True
    desired_caps['automationName'] = 'UiAutomator2'

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    return driver

