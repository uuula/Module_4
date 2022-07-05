from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL_ADDRESS = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD_1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD_2 = (By.NAME, "registration-password2")


class ProductPageLocators():
    DROPDOWN_ITEM = (By.CSS_SELECTOR, "[href='/ru/catalogue/']")
    PRODUCT_LINK = (By.CSS_SELECTOR, "[alt='The shellcoder's handbook']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[value='Add to basket']")
    MESSAGE_TEXT_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BOOK_NAME_LINK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > "
                                     "p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span > a")


class BasketPageLocators():
    TEXT_IN_BASKET_WHEN_PRODUCT_IS_ADDED = (By.CSS_SELECTOR, "div.basket-title.hidden-xs > div > h2")
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
