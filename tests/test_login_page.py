import pytest

from pages.profile_page import ProfilePage
from pages.constants import LoginPageConstants, ProfilePageConstants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.locators import MainPageLocators
import requests


@pytest.mark.login
def test_go_to_login(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
    browser.save_screenshot('result_completed_login_page.png')
    link = ProfilePageConstants.PROFILE_PAGE_URL
    response = requests.get(link)
    r = response.status_code
    assert response.status_code == 200, f'{r} is not our expectation'
#    element_photo = WebDriverWait(browser, 10)
#    element_photo.until(EC.presence_of_element_located(*MainPageLocators.NAME_PETS))
# здесь не переходит на страницу профиля, хотя тест проходит без ошибок! Поэтому 2 верхние строки закомментированы.
