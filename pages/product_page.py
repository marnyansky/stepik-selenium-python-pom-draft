from .base_page import BasePage
from .locators import ProductPageLocators

product_name = ""
product_price = ""


class ProductPage(BasePage):

    def remember_product_name_and_price_and_add_product_to_basket(self):
        # Занесение названия продукта и его цены в глобальные переменные
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def product_should_be_in_basket_with_the_same_name_and_the_same_price(self):
        # Проверка сообщений с ключевыми элементами: название продукта, цена продукта
        expected_product_added_message = self.product_name + " has been added to your basket."
        actual_product_added_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert expected_product_added_message == actual_product_added_message, \
            "The product added to basket has different name"

        expected_basket_total_message = "Your basket total is now " + self.product_price
        actual_basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert expected_basket_total_message == actual_basket_total_message, \
            "The product added to basket has different price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE) == True, \
            "Success message is present, though it shouldn't"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE) == True, \
            "Success message is present, though it shouldn't"

    def should_be_able_to_go_to_login_page(self):
        self.go_to_login_page()
        assert "login" in self.browser.current_url, "Wrong URL - do not contains 'login'"
