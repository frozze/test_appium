from appium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Authorization:
    def __init__(self):
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "Android Emulator",
            "app": "/home/frozze/PycharmProjects/pythonProject/appiutest/st3.apk",
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

        self.driver.implicitly_wait(20)
        element_to_tap = self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/ordersButton")
        element_to_drag_to = self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/profileImageView")
        self.driver.scroll(element_to_tap, element_to_drag_to)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/logoutButton").click()
        # self.driver.find_element(By.ID, "android:id/button2").click()  #Отмена
        self.driver.find_element(By.ID, "android:id/button1").click()  #OK


login = Authorization()
login.log()
