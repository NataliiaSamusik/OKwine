from constants.start_page import StartPageConst
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_wrapper


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst

    @wait_until_ok(timeout=10, period=1)
    @log_wrapper
    def confirm_age(self):
        """Confirm age"""
        self.click(xpath=self.const.YES_BUTTON_XPATH)

    @log_wrapper
    def verify_start_page_opened(self):
        """Verify Start page opened"""
        assert self.compare_element_text(xpath=self.const.START_PAGE_BESTSELERS_XPATH,
                                         text=self.const.START_PAGE_BESTSELERS_TEXT)

    @log_wrapper
    def navigate_to_import_page(self):
        """Navigate to Import page"""
        self.click(xpath=self.const.MENU_XPATH)
        self.click(xpath=self.const.IMPORT_XPATH)

        from pages.import_page import ImportPage
        return ImportPage(self.driver)

    @log_wrapper
    def navigate_to_product_page(self):
        """Navigate to product page"""
        self.click(xpath=self.const.PRODUCT_INFO_XPATH)

        from pages.product_page import ProductPage
        return ProductPage(self.driver)

    @log_wrapper
    def empty_login_page(self, user):
        """Try to login with empty login field"""
        self.click(xpath=self.const.MENU_XPATH)
        self.click(xpath=self.const.LOGIN_XPATH)
        # self.fill_field(xpath=self.const.SIGN_IN_EMAIL_FIELD_XPATH, value=user.email)
        # self.fill_field(xpath=self.const.SIGN_IN_PASSWORD_FIELD_XPATH, value=user.password)
        self.click(self.const.SIGN_IN_BUTTON_XPATH)

    @log_wrapper
    def verify_error_empty_login_page(self):
        """Verify ERROR for empty login field"""
        assert self.is_element_exists(xpath=self.const.ERROR_LOGIN_XPATH)

    @log_wrapper
    @wait_until_ok(timeout=10, period=1)
    def sign_up_empty_email(self, user):
        """Sign up using provided values"""
        self.click(xpath=self.const.MENU_XPATH)
        self.click(xpath=self.const.LOGIN_XPATH)
        self.click(xpath=self.const.SIGN_UP_WINDOW_XPATH)
        self.fill_field(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_field(xpath=self.const.SIGN_UP_SURNAME_FIELD_XPATH, value=user.surname)
        self.fill_field(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=user.password)
        self.fill_field(xpath=self.const.SIGN_UP_CONFIRM_PASSWORD_FIELD_XPATH, value=user.password)
        self.click(self.const.SIGN_UP_BUTTON_XPATH)

    @log_wrapper
    def verify_error_empty_email(self):
        """Verify Error for empty Email field"""
        assert self.compare_element_text(xpath=self.const.ERROR_EMPTY_EMAIL_XPATH,
                                         text=self.const.ERROR_EMPTY_EMAIL_TEXT)

    @log_wrapper
    def unconfirm_age(self):
        """UNconfirm age"""
        self.click(xpath=self.const.NO_BUTTON_XPATH)

        from pages.unconfirm_age_page import UnconfirmPage
        return UnconfirmPage(self.driver)

    @log_wrapper
    def basket_by_default(self):
        """How does basket page look by default"""
        self.click(xpath=self.const.BASKET_ICON_XPATH)

        from pages.basket_page import BasketPage
        return BasketPage(self.driver)
