import logging
from pytest import fixture
from typing import Any, Generator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium_project.pages.login import LoginPage
from selenium_project.pages.dropdown import DropDownPage
from selenium_project.pages.date_picker import DatePicker
from selenium_project.pages.file_upload import FileUpload
from selenium_project.pages.slider import Slider
from selenium_project.pages.web_table import WebTable


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests against"
    )


@fixture
def browser(request) -> str:
    return request.config.getoption("--browser")

@fixture
def driver(browser):
    """
    This fixture initializes a WebDriver for the specified browser,
     and ensures proper cleanup after the test execution by quitting the driver.
    """
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    yield driver
    driver.quit()

@fixture
def slider(driver) -> Slider:
    return Slider(driver)

@fixture
def dropdown_page(driver) -> DropDownPage:
    return DropDownPage(driver)

@fixture
def file_upload(driver) -> FileUpload:
    return FileUpload(driver)

@fixture
def date_picker(driver) -> DatePicker:
    driver.refresh()
    return DatePicker(driver)

@fixture
def web_table(driver) -> WebTable:
    return WebTable(driver)

@fixture
def login_page()-> Generator[LoginPage, Any, None]:
    """This fixture instantiates the login page."""
    logging.debug("Initializing Chrome WebDriver")
    chrome_driver = webdriver.Chrome()
    login = LoginPage(chrome_driver)
    logging.debug("Starting test execution")
    yield login
    chrome_driver.close()

@fixture(
    params=['Jan', 'Feb', 'Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    ids=lambda c: c)
def month(request):
    """, 'Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'"""
    return request.param
