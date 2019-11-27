from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest

@pytest.mark.parametrize('number', [0, 1, 2, 3, 4, pytest.param(5, marks=pytest.mark.xfail), 6, 7, 8, 9])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()
    page.get_product_to_the_basket()
    page.solve_quiz_and_get_code()
    page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    page.is_element_present(*ProductPageLocators.BUSKET_TOTAL)

    