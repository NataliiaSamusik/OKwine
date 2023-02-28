from constants.unconfirm_age_page import UnconfirmPageConst
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_wrapper


class UnconfirmPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = UnconfirmPageConst

    @log_wrapper
    def verify_google_unconfirm(self):
        """Verify Error for empty Email field"""
        assert self.is_element_exists(xpath=self.const.UNCONFIRM_AGE_PAGE_XPATH)
