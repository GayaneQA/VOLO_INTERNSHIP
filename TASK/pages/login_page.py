from selenium.webdriver.common.by import By
from utils.helpers import Helper
from utils.config import USERNAME, PASSWORD


class LoginPage(Helper):
    username_field = (By.XPATH, "//input[@id='signInName']", "Username input")
    password_field = (By.XPATH, "//input[@id='password']", "Password input")
    signin_button = (By.XPATH, "//button[@id='next']", "Sign in button")

    def login(self, username=USERNAME, password=PASSWORD):
        self.send_keys(self.username_field, username)
        self.send_keys(self.password_field, password)
        self.click(self.signin_button)
