"""Tests related to start page"""
import logging

import pytest

from conftest import start_page, product_page
from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestStartPage:
    """Stores tests for start page """

    # Open Product page via basket page
    def test_confirm_age(self, start_page, confirm_age):
        """
        - Pre-conditions:
            - Open start page
            - Confirm age
        - Steps:
            - Verify Start page
        """
        # Verify Start page
        start_page.verify_start_page_opened()

    def test_import_page(self, start_page, confirm_age):
        """
        - Pre-conditions:
            - Open start page
            - Confirm age
        - Steps:
            - Navigate to Import page via Menu
            - Verify Import page
        """
        # Navigate to Import page via Menu
        import_page = start_page.navigate_to_import_page()
        # Verify Import page
        import_page.verify_import_page_opened()

    def test_product_page(self, start_page, confirm_age):
        """
        - Pre-conditions:
            - Open start page
            - Confirm age
        - Steps:
            - Click on any Product
            - Verify that correct page is opened
        """
        # Click on any Product
        product_page = start_page.navigate_to_product_page()
        # Verify that correct page is opened
        product_page.verify_product_page_opened()

    def test_login_empty_user(self, start_page, confirm_age, random_user):
        """
        - Pre-conditions:
            - Open start page
            - Confirm age
        - Steps:
            - Leave email field empty
            - Leave password field empty
            - Click on Login button
            - Verify error
        """
        # Leave fields empty/Click on Login button
        start_page.empty_login_page(random_user)
        # Verify error
        start_page.verify_error_empty_login_page()

    def test_sign_up_empty_email(self, start_page, confirm_age, random_user):
        """
        - Pre-conditions:
            - Open start page
            - Confirm age
        - Steps:
            - Leave email field empty
            - Click on Sign up button
            - Verify error
        """
        # Leave field email empty/Click on sign up button
        start_page.sign_up_empty_email(random_user)
        # Verify error
        start_page.verify_error_empty_email()
