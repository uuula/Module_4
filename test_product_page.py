import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)  # инициализируем Page Object, передаём в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_add_product_to_cart()
    product_page.should_product_name_in_cart_and_message_are_the_same()
    product_page.should_basket_cost_is_the_same_as_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаём в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_add_product_to_cart()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаём в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаём в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_add_product_to_cart()
    product_page.should_element_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_basket_is_empty()
    page.should_be_text_message_about_basket_empty()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаём в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = MainPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_add_product_to_cart()
        product_page.should_product_name_in_cart_and_message_are_the_same()
        product_page.should_basket_cost_is_the_same_as_product_price()
