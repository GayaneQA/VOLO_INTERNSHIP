from selenium.webdriver.common.by import By
from utils.helpers import Helper


class DashboardPage(Helper):
    doas_nav = (
        By.XPATH,
        "//div[contains(@class,'user-nav__item')]//span[text()='DoAs']",
        "DoAs navigation")
    new_doa_button = (
        By.XPATH,
        "//button[@data-testid='topbar-msal-newDoa']",
        "New DoA button")

    def open_doas_page(self):
        self.click(self.doas_nav)

    def click_new_doa(self):
        self.click(self.new_doa_button)
