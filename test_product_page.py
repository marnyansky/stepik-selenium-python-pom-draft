from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.remember_product_name_and_price_and_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_should_be_in_basket_with_the_same_name_and_the_same_price()
