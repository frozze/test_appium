from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Android Emulator",
    "app": "/home/frozze/PycharmProjects/pythonProject/app/Wikipedia.com.apk"}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

driver.implicitly_wait(5)

driver.find_element(By.ID, "org.wikipedia:io/search_container").click()
