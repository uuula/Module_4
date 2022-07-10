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

    def register_new_user(self, email, password):

        registration_email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_email_field.send_keys(email)

        registration_password_field_1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1)
        registration_password_field_1.send_keys(password)

        registration_password_field_2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2)
        registration_password_field_2.send_keys(password)

        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()