Selenium Test Automation Framework

Overview

This Automation Framework is a modular UI testing suite, built with Python, Selenium WebDriver, and Pytest, following the Page Object Model (POM) design pattern.

This framework automates:

Host entity login flows
Navigation to the DoAs (Description of Assignment) section
Online DoA form creation and submission
Validation of success messages and user actions
It’s designed for maintainability, scalability, and clarity — allowing new tests or pages to be added with minimal effort.

Project Structure

TASK/
│
├── pages/                              # Page Object classes
│   ├── dashboard_page.py               # Dashboard interactions (navigation, DoA creation)
│   ├── doa_creation_page.py            # DoA form creation and submission
│   ├── home_page.py                    # Landing page (login entry point)
│   └── login_page.py                   # Login flow (username, password, sign-in)
│
├── tests/
│   └── test_doa_creation_online.py     # End-to-end test for online DoA creation
│
├── utils/
│   ├── config.py                       # Environment variables (URL, credentials)
│   ├── driver_setup.py                 # Chrome driver configuration
│   ├── helpers.py                      # Common Selenium interaction helpers
│   └── test_data.py                    # Static data for form filling
│
├── conftest.py                         # Pytest fixtures (driver, logger)
├── requirements.txt                    # Dependency list
├── venv/                               # Virtual environment
└── README.md                           # Project documentation
