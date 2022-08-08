from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# SCROLL_DUR_MS = 3000


class Authorization:
    def __init__(self):
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "Android Emulator",
            "app": "/home/pavel/Документы/appiutest/st3.apk",
            "noReset": True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

    def log(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "ru.tokyocity.tokyocity.stage3:id/more"))
        )
        element.click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/loginButton").click()
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/phoneEditText").send_keys("1234567894")
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/getCodeButton").click()
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/editText").send_keys("1234")
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/logoutButton")
        # self.scroll_page()

    # def scroll_page(self):
    #     self.driver.swipe(150, 400, 150, 200, 1000)


login = Authorization()
login.log()
