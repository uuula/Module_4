from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, "There is no 'login' substring in the current browser url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_ADDRESS), "Login email field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password field is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email field is not " \
                                                                               "presented "
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_1), "Registration password field is " \
                                                                                    "not presented "
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_2), "Registration repeat password " \
                                                                                    "field is not presented"

