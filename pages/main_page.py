import time
from selenium.webdriver import Keys
from .locators import MainPageLocators
from .base_page import BasePage
from .constants import MainPageConstants


class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        # звездочка означает, что передали пару "ключ - значение" и этот картеж надо распаковать
        time.sleep(3)
        assert True
        self.browser.find_element(*MainPageLocators.ICON), 'Иконка находится в шапке сайта и видна всегда!'

    def use_filter_by_type(self):
        self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE_LINK).click()
        assert True
        self.browser.find_element(*MainPageLocators.ICON), 'Иконка находится в шапке сайта и видна всегда!'

    def select_dog(self):
        self.browser.find_element(*MainPageLocators.DOG_LINK).click()

    def use_filter_by_name_Rex(self):
        name_dog = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME_LINK)
        name_dog.send_keys(MainPageConstants.DOG_NAME)
        name_dog.send_keys(Keys.ENTER)
        time.sleep(4)

        assert len(self.browser.find_elements(*MainPageLocators.NAME_PETS)) == 1

    def go_to_details_pet(self):
        self.browser.find_element(*MainPageLocators.DETAILS_BUTTON).click()
        time.sleep(4)

        assert True
        self.browser.find_element(*MainPageLocators.ICON), 'Иконка находится в шапке сайта и видна всегда!'

    #        assert self.browser.find_element(*MainPageLocators.OWNER) == 'natali1793@mail.ru'

    def select_cat(self):
        self.browser.find_element(*MainPageLocators.CAT_LINK).click()

    def use_filter_by_name_Domna(self):
        name_cat = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME_LINK)
        name_cat.clear()
        name_cat.send_keys(MainPageConstants.CAT_NAME)
        name_cat.send_keys(Keys.ENTER)
        time.sleep(4)

        assert len(self.browser.find_elements(*MainPageLocators.NAME_PETS)) == 1

    def select_hamster(self):
        self.browser.find_element(*MainPageLocators.HAMSTER_LINK).click()

    def use_filter_by_name_Banny(self):
        name_hamster = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME_LINK)
        name_hamster.clear()
        name_hamster.send_keys(MainPageConstants.HAMSTER_NAME)
        name_hamster.send_keys(Keys.ENTER)
        time.sleep(4)

        assert len(self.browser.find_elements(*MainPageLocators.NAME_PETS)) == 1
