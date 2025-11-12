from utils.config import BASE_URL
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.doa_creation_page_online import DoaCreationPage
from utils.test_data import DOA_FORM_DATA


def test_create_online_doa(test_driver, test_logger):

    home_page = HomePage(test_driver, test_logger)
    login_page = LoginPage(test_driver, test_logger)
    dashboard = DashboardPage(test_driver, test_logger)
    doa_page = DoaCreationPage(test_driver, test_logger)

    test_driver.get(BASE_URL)
    test_driver.maximize_window()
    home_page.click_login_button()
    login_page.login()

    dashboard.open_doas_page()
    dashboard.click_new_doa()
    doa_page.fill_doa_form(DOA_FORM_DATA)
    doa_page.submit_doa()

    success_text = doa_page.get_success_message()
    assert "successfully submitted" in success_text.lower()
