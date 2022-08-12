from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from desired_caps.capabilities import android_11


class TestAuthorization:
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=android_11())

    @pytest.mark.st_change
    def test_log_in(self):
        # try:
        #     self.geo = WebDriverWait(self.driver, 20).until(
        #         EC.presence_of_element_located(
        #             (By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"))
        #     )
        #     self.geo.click()
        #     self.city = WebDriverWait(self.driver, 20).until(
        #         EC.presence_of_element_located(
        #             (By.XPATH, "//*[contains(@text, 'Санкт-Петербург')]"))
        #     )
        #     self.city.click()
        # finally:
        self.element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "ru.tokyocity.tokyocity.test:id/more"))
        )
        self.element.click()
        self.driver.find_element(By.XPATH, "//*[contains(@content-desc, 'Отладочное меню')]").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/serverSettingsButton").click()
        self.driver.find_element(By.XPATH, "//android.widget.EditText").send_keys("https://back-tc-stg3.fssoft.ru/")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//android.widget.Button[contains(@content-desc, 'Сохранить')]").click()
        self.driver.implicitly_wait(5)
