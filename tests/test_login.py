"""
Test cases for Login functionality
"""

import pytest
from pages.login_page import LoginPage


class TestLogin:
    """
    Login test suite
    """

    def test_valid_login(self, setup):
        """
        Verify successful login with valid credentials
        """
        driver = setup
        login_page = LoginPage(driver)

        login_page.login("tomsmith", "SuperSecretPassword!")
        message = login_page.get_flash_message()

        assert "You logged into a secure area!" in message

    @pytest.mark.parametrize(
        "username,password",
        [
            ("invalid", "SuperSecretPassword!"),
            ("tomsmith", "wrongpass"),
        ],
    )
    def test_invalid_login(self, setup, username, password):
        """
        Verify login fails with invalid credentials
        """
        driver = setup
        login_page = LoginPage(driver)

        login_page.login(username, password)
        message = login_page.get_flash_message()

        assert "Your username is invalid!" in message or "Your password is invalid!" in message