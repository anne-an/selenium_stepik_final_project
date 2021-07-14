from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART_BUTTON).click()

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_added_to_cart(self, title, price):
        assert title == self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_TITLE).text, "The product title is wrong"
        assert price == self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text, "The product price is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message does not disappear, but it should"
