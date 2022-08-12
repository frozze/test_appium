
def android_11():
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "Android Emulator",
        "app": "/home/pavel/Documents/test_login_android/apps/ТОКИО-CITY-TEST.apk",
        "noReset": True
    }
    return desired_capabilities


def redmi_note_4():
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "7",
        "uid": "2a1958850904",
        "deviceName": "Xiaomi Redmi Note 4",
        "app": "/home/pavel/Documents/test_login_android/apps/ТОКИО-CITY-TEST.apk",
        # "noReset": True
    }
    return desired_capabilities
