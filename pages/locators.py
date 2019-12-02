from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, "basket")


class BasketPageLocators(BasePageLocators):
    CONTENT_INNER_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    CONTENT_INNER = (By.CSS_SELECTOR, "#content_inner")
    BASKET_SUMMARY = (By.CSS_SELECTOR, ".basket_summary")


class MainPageLocators(BasePageLocators):
    pass


class LoginPageLocators(BasePageLocators):
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators(BasePageLocators):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner > strong")
    BUSKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner > p > strong")