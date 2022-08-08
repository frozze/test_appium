from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# SCROLL_DUR_MS = 3000


class Authorization:
    def __init__(self):
        self.element = None
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "7",
            "uid": "2a1958850904",
            "deviceName": "Xiaomi Redmi Note 4",
            "app": "/home/pavel/Документы/appiutest/st3.apk",
            "noReset": True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

    def log(self):
        lst = []
        self.element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "ru.tokyocity.tokyocity.stage3:id/more"))
        )
        self.element.click()
        
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/loginButton").click()
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/phoneEditText").send_keys("1234567894")
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/getCodeButton").click()
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/editText").send_keys("1234")
        self.driver.implicitly_wait(15)
        self.driver.swipe(470, 1400, 470, 950, 330)
        # lst = self.driver.find_element(By.ID, 'com.abc.android.abc:id/common_tab_list')
        # action = TouchAction(self.driver)
        # for i in range(0, 10):
        #     action.press(x=750, y=1750).move_to(x=0, y=-75).perform()
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/logoutButton")

    def get_myWindow_size(self):

        x = self.driver.get_window_size()['width']  # Get the length of the x axis
        y = self.driver.get_window_size()['height']  # Get the length of the y axis

        return x, y


login = Authorization()
print(login.get_myWindow_size())
login.log()
