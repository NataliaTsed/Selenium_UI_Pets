from .constants import ProfilePageConstants
from .base_page import BasePage
from .locators import MainPageLocators
from selenium import webdriver


class ProfilePage(BasePage):

    def check_the_number_of_pets(self):
        assert len(self.browser.find_elements(*MainPageLocators.NAME_PETS)) == 3, 'У меня всего 3 питомца!'
