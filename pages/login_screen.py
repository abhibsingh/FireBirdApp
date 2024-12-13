from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "username")
    PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "password")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "loginButton")

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
