from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)


    def no_orders_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_SUMMARY)


    def empty_is_present_in_message(self):
        assert "empty" in self.get_text_from_element(*BasketPageLocators.CONTENT_INNER_MESSAGE)