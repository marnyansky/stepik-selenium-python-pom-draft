import mimesis
import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.xfail(raises=AssertionError, reason="test should xfail (Stepik.org course > module 4.3.6)")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.remember_product_name_and_price_and_add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail(raises=AssertionError, reason="test should xfail (Stepik.org course > module 4.3.6)")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.remember_product_name_and_price_and_add_product_to_basket()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_able_to_go_to_login_page()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        reg_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, reg_link)
        page.open()
        page.should_be_register_form()

        f_person = mimesis.Person()
        f_email = f_person.email(domains=['mimesis.name'], unique=True)
        f_password = f_person.password(length=10, hashed=False)
        page.register_new_user(f_email, f_password)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.remember_product_name_and_price_and_add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.product_should_be_in_basket_with_the_same_name_and_the_same_price()
