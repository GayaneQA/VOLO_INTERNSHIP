from selenium.webdriver.common.by import By
from utils.helpers import Helper


class HomePage(Helper):
    login_button = (
        By.XPATH,
        "//button[contains(@class,'topbar-login')]",
        "Login button")

    def click_login_button(self):
        self.click(self.login_button)
