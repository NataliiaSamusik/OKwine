from constants.import_page import ImportPageConst
from pages.base_page import BasePage
from pages.utils import log_wrapper

class ImportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = ImportPageConst

    @log_wrapper
    def verify_import_page_opened(self):
        """Verify Import page opened"""
        assert self.is_element_exists(xpath=self.const.IMPORT_PAGE_XPATH)



