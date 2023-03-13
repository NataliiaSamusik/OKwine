from constants.basket_page import BasketPageConst
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_wrapper


class BasketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = BasketPageConst

    @log_wrapper
    def verify_basket_page_empty_by_default(self):
        """Verify Start page opened"""
        assert self.compare_element_text(xpath=self.const.EMPTY_BASKET_XPATH,
                                         text=self.const.EMPTY_BASKET_TEXT)
