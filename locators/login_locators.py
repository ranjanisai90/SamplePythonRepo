from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginBtn")