from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from desired_caps.capabilities import redmi_note_4


class TestAuthorization:
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=redmi_note_4())

    @pytest.mark.log_logout
    @pytest.mark.login
    def test_log_in(self):
        print('Login test started')
        self.geo = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "com.android.packageinstaller:id/permission_allow_button"))
                # (By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"))
        )
        self.geo.click()
        self.city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(@text, 'Санкт-Петербург')]"))
        )
        self.city.click()
        self.element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "ru.tokyocity.tokyocity.test:id/more"))
        )
        self.element.click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/loginButton").click()
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/phoneEditText").send_keys("1234567892")
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/getCodeButton").click()
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/editText").send_keys("2234")
        assert self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/ordersButton") != 0, \
            "Authorization test failed"

    @pytest.mark.log_logout
    @pytest.mark.logout
    def test_log_out(self):
        self.element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "ru.tokyocity.tokyocity.test:id/more"))
        )
        self.element.click()
        element_to_tap = self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/ordersButton")
        element_to_drag_to = self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/profileImageView")
        self.driver.scroll(element_to_tap, element_to_drag_to)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/logoutButton").click()
        self.driver.find_element(By.ID, "android:id/button2").click()  #Отмена
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/logoutButton").click()
        self.driver.find_element(By.ID, "android:id/button1").click()  # OK
        assert self.driver.find_element(By.ID, "ru.tokyocity.tokyocity.test:id/loginButton") != 0, \
            "Logout test failed"
