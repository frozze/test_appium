def android_11():
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "Android Emulator",
        "app": "C:\\Users\FroZZe\Documents\\test_appium\\apps\\TOKIO_CITY_TEST1421.apk",
        "noReset": True
    }
    return desired_capabilities

# def redmi_note_4():
#     desired_capabilities = {
#         "platformName": "Android",
#         "platformVersion": "7",
#         "uid": "2a1958850904",
#         "deviceName": "Xiaomi Redmi Note 4",
#         "app": "/home/frozze/PycharmProjects/test_appium/apps/ТОКИО-CITY-TEST.apk",
#         # "noReset": True
#     }
#     return desired_capabilities
