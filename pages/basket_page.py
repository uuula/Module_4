from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.TEXT_IN_BASKET_WHEN_PRODUCT_IS_ADDED), \
            "A product is presented in the basket, but should not be"

    def should_be_text_message_about_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_IS_EMPTY), "Empty basket message is not present"
