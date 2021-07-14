from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, url)
    product_page.open(url)
    title = product_page.get_product_title()
    price = product_page.get_product_price()
    product_page.add_to_cart()
    product_page.should_be_added_to_cart(title, price)
