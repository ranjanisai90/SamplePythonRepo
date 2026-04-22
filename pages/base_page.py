"""
Base Page containing reusable Selenium actions
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    BasePage provides common methods for all pages
    """

    def __init__(self, driver, timeout=10):
        """
        Initialize BasePage

        :param driver: WebDriver instance
        :param timeout: wait timeout
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        """
        Find element

        :param locator: tuple (By, value)
        :return: WebElement
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """
        Click element

        :param locator: tuple (By, value)
        """
        self.find(locator).click()

    def send_keys(self, locator, text):
        """
        Enter text

        :param locator: tuple (By, value)
        :param text: input text
        """
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Get text of element

        :param locator: tuple (By, value)
        :return: text
        """
        return self.find(locator).text