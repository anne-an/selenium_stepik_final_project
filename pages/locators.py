from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-username")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[value=\"Log In\"]")

    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_REPEAT = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[value=\"Register\"]")


class ProductPageLocators:
    PRODUCT_ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    ADDED_PRODUCT_TITLE = (By.CSS_SELECTOR, ".alertinner strong")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")
