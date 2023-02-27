import pytest

from pages.start_page import StartPage
from pages.utils import create_driver

from pages.values import User

@pytest.fixture()
def driver(browser):
    """Creates selenium driver"""
    driver = create_driver(browser=browser)
    yield driver
    driver.close()


@pytest.fixture()
def start_page(driver):
    """Creates start page object"""
    return StartPage(driver)

@pytest.fixture()
def confirm_age(start_page):
    confirm_age = start_page.confirm_age()
    return confirm_age

@pytest.fixture()
def product_page(start_page):
    """Navigate to PRODUCT page"""
    product_page = start_page.go_to_products_by_basket()
    return product_page


@pytest.fixture()
def empty_user():
    """Creates an empty user"""
    return User()

@pytest.fixture()
def random_user(empty_user):
    """Creates random user"""
    empty_user.fill_data()
    return empty_user
