import logging
import os
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def test_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def test_logger(request):
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)
    logger_name = request.node.name
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        file_path = os.path.join(logs_dir, f"{logger_name}.log")
        file_handler = logging.FileHandler(file_path, mode="w")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
