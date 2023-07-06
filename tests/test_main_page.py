import pytest
from pages.main_page import MainPage
from pages.constants import MainPageConstants


# с главной страницы переходит на страницу Login
def test_go_to_login_page(browser):
    link = MainPageConstants.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('result_login_page.png')


# проверяю всех своих питомцев, которые созданные в моем аккаунте
@pytest.mark.filters
def test_choose_pet(browser):
    link = MainPageConstants.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.use_filter_by_type()
    page.select_dog()
    page.use_filter_by_name_Rex()
    browser.save_screenshot('result_pet_dog.png')
    page.use_filter_by_type()
    page.select_cat()
    page.use_filter_by_name_Domna()
    browser.save_screenshot('result_pet_cat.png')
    page.use_filter_by_type()
    page.select_hamster()
    page.use_filter_by_name_Banny()
    browser.save_screenshot('result_pet_hamster.png')


@pytest.mark.details
def test_go_to_details_dog(browser):
    link = MainPageConstants.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.use_filter_by_type()
    page.select_dog()
    page.use_filter_by_name_Rex()
    page.go_to_details_pet()


@pytest.mark.details
def test_go_to_details_cat(browser):
    link = MainPageConstants.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.use_filter_by_type()
    page.select_cat()
    page.use_filter_by_name_Domna()
    page.go_to_details_pet()


@pytest.mark.details
def test_go_to_details_hamster(browser):
    link = MainPageConstants.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.use_filter_by_type()
    page.select_hamster()
    page.use_filter_by_name_Banny()
    page.go_to_details_pet()
