from constants.product_page import ProductPageConst
from pages.base_page import BasePage
from pages.utils import log_wrapper

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = ProductPageConst

    @log_wrapper
    def verify_product_page_opened(self):
        """Verify Product page opened"""
        assert self.compare_element_text(xpath=self.const.PRODUCT_PAGE_XPATH, text=self.const.PRODUCT_PAGE_TEXT)