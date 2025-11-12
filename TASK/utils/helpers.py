from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException


class Helper:
    def __init__(self, driver, logger=None, timeout=60):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout

    def click(self, locator, scroll=True, timeout=None):
        timeout = timeout or self.timeout
        by, value, name = locator
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value)))
            if scroll:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", elem)
            self.driver.execute_script("arguments[0].click();", elem)
            if self.logger:
                self.logger.info(f"Clicked element: {name}")
        except (TimeoutException, WebDriverException) as e:
            if self.logger:
                self.logger.info(
                    f"Failed to click element: {name} | Error: {e}")
            raise

    def send_keys(self, locator, text, click_first=True, timeout=None):
        timeout = timeout or self.timeout
        by, value, name = locator
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value)))
            if click_first:
                try:
                    elem.click()
                except WebDriverException:
                    self.driver.execute_script("arguments[0].click();", elem)
            elem.clear()
            elem.send_keys(text)
            entered_value = elem.get_attribute("value")
            if not entered_value or entered_value.strip() == "":
                self.driver.execute_script(
                    "arguments[0].value = arguments[1];", elem, text)
                if self.logger:
                    self.logger.info(f"Used JS fallback for {name}")
            if self.logger:
                self.logger.info(f"Sent keys '{text}' to element: {name}")
        except (TimeoutException, WebDriverException) as e:
            if self.logger:
                self.logger.info(
                    f"Failed to send keys to element: {name} | Error: {e}")
            raise

    def get_element(self, locator, timeout=None):
        timeout = timeout or self.timeout
        by, value, name = locator
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value)))
            if self.logger:
                self.logger.info(f"Located element: {name}")
            return elem
        except (TimeoutException, WebDriverException) as e:
            if self.logger:
                self.logger.info(
                    f"Failed to locate element: {name} | Error: {e}")
            raise

    def click_template(self, locator_template, value):
        by, template_str, name = locator_template
        locator = (by, template_str.format(value), f"{name}: {value}")
        self.click(locator)
