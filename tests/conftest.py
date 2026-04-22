"""
Pytest fixtures setup
"""

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config.config import Config


@pytest.fixture(scope="session")
def driver():
    """
    Initialize WebDriver instance

    :return: WebDriver
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def setup(driver):
    """
    Setup test preconditions

    :param driver: WebDriver fixture
    :return: driver
    """
    driver.get(Config.BASE_URL)
    return driver