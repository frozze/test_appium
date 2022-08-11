from appium import webdriver


def driver11():
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "Android Emulator",
        "app": "/home/pavel/Documents/test_login_android/st3.apk",
        # "noReset": True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    return driver
