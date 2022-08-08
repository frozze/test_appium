from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Android Emulator",
    "app": "/home/pavel/Документы/appiutest/st3.apk",
    "noReset": True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
driver.implicitly_wait(20)
element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "ru.tokyocity.tokyocity.stage3:id/cart"))
)
element.click()
driver.implicitly_wait(10)
driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/cart").click()
driver.find_element(By.ID, "ru.tokyocity.tokyocity.stage3:id/clearCart").click()
driver.find_element(By.ID, "android:id/button1").click()
