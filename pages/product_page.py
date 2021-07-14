from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART_BUTTON).click()
        self.solve_quiz_and_get_code()

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_added_to_cart(self, title, price):
        assert title == self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_TITLE).text, "The product title is wrong"
        assert price == self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text, "The product price is wrong"
