
def android_11():
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "Android Emulator",
        "app": "/home/frozze/PycharmProjects/appiutest/st3.apk",
        # "noReset": True
    }
    return desired_capabilities
