import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()

    def should_product_name_in_cart_and_message_are_the_same(self):
        message_text = self.browser.find_element(*ProductPageLocators.MESSAGE_TEXT_LINK).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_LINK).text
        assert message_text == book_name, "The book name does not match what was added to the cart"

    def should_basket_cost_is_the_same_as_product_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert book_price == basket_cost, "Product price and cart price don't match"
