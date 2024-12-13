from appium import webdriver

def test_launch_app():
    # Configuration for Appium
    desired_capabilities = {
  "platformName": "Android",
  "appium:deviceName": "OnePlus Nord 2T",
  "appium:udid": "CYINPR4PIV6PJNKF",
  "appium:appPackage": "com.firebird.artist360.uat",
  "appium:appActivity": "com.firebird.artist360.MainActivity",
  "appium:automationName": "UiAutomator2",
  "appium:ignoreHiddenApiPolicyError": True,
  "appium:noReset": True
}

    # Initialize the Appium driver
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)

    try:
        # Validate that the app launched successfully
        assert driver.is_app_installed("com.firebird.artist360.uat")  # Replace with your app's package name
    finally:
        # Quit the driver
        driver.quit()
