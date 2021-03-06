from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Registration email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Registration password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_REPEAT), "Registration repeat password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Registration button is not presented"

    def register_new_user(self, login, password):
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(login)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
