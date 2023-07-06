from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, 'div#app > header > div > ul > li > a > span')
    FILTER_BY_TYPE_LINK = (By.CSS_SELECTOR, 'span#typesSelector')
    FILTER_BY_NAME_LINK = (By.CSS_SELECTOR, 'input#petName')
    DOG_LINK = (By.CSS_SELECTOR, '#pv_id_2_0')
    CAT_LINK = (By.CSS_SELECTOR, '#pv_id_2_1')
    HAMSTER_LINK = (By.CSS_SELECTOR, '#pv_id_2_3')
    FIELD_LINK = (By.CSS_SELECTOR, 'div#app')
    # FIELD LINK заменяет нажатие Enter, т.к. после вставки текста clic не работает должным образом
    NAME_PETS = (By.CSS_SELECTOR, ".col-12")
    DETAILS_BUTTON = (By.CSS_SELECTOR,
                      'div#app > main > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div:nth-of-type(3) > div > button')
#    OWNER = (By.CLASS_NAME, 'flex flex-column')
    ICON = (By.CSS_SELECTOR, '#app > header > div > div > img')


class LoginPagesLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BUTTON = (By.CLASS_NAME, "p-button-label")
    LOGIN_LOGO = (By.CSS_SELECTOR, '#app > main > fieldset > legend')


class ProfilePagesLocators:
    PHOTO_PET = (By.CSS_SELECTOR,
                 '#app > main > div > div > div.p-dataview-content > div > div:nth-child(2) > div > img')
