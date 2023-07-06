import time

from pages.constants import LoginPageConstants
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


def test_check_my_pets(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
#    link = 'http://34.141.58.52:8080/#/profile'
#    page1 = ProfilePage(browser, page)
#    page.open()
#    page1.check_the_number_of_pets()
#    time.sleep(4)
