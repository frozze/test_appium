
def android_11():
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "Android Emulator",
        "app": "/home/pavel/Documents/test_login_android/st3.apk",
        # "noReset": True
    }
    return desired_capabilities
