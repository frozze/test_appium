from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from desired_caps.capabilities import android_11


class TestAuthorization:
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=android_11())

    @pytest.mark.order
    def test_order(self):

        self.element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "ru.tokyocity.tokyocity.test:id/more"))
        )
        self.element.click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/loginButton").click()
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/phoneEditText").send_keys("1234567894")
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/getCodeButton").click()
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/editText").send_keys("2234")
        assert self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/ordersButton") != 0, \
            "Authorization test failed"
