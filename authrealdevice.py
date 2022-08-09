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

        element_to_tap = self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/ordersButton")
        element_to_drag_to = self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/profileImageView")
        self.driver.scroll(element_to_tap, element_to_drag_to)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/logoutButton").click()
        # self.driver.find_element(By.ID, "android:id/button2").click()  #Отмена
        self.driver.find_element(By.ID, "android:id/button1").click()  # OK

    def get_myWindow_size(self):

        x = self.driver.get_window_size()['width']  # Get the length of the x axis
        y = self.driver.get_window_size()['height']  # Get the length of the y axis

        return x, y


login = Authorization()
login.log()
