"""
Login Page Object
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for Login Page
    """

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MSG = (By.ID, "flash")

    def login(self, username: str, password: str):
        """
        Perform login action

        :param username: username
        :param password: password
        """
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_flash_message(self) -> str:
        """
        Get login result message

        :return: message text
        """
        return self.get_text(self.FLASH_MSG)