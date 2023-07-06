import time
from .base_page import BasePage
from .locators import LoginPagesLocators
from .constants import LoginPageConstants


class LoginPage(BasePage):
    def go_to_login(self):
        self.browser.find_element(*LoginPagesLocators.LOGIN_EMAIL).send_keys(LoginPageConstants.LOGIN_EMAIL)
        time.sleep(3)

    def go_to_password(self):
        self.browser.find_element(*LoginPagesLocators.LOGIN_PASSWORD).send_keys(LoginPageConstants.LOGIN_PASSWORD)
        time.sleep(3)

    def go_to_button(self):
        self.browser.find_element(*LoginPagesLocators.LOGIN_BUTTON).submit()
        time.sleep(3)
