import pytest
import logging
from pytest import fixture
from typing import Any, Generator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium_project.pages.login import LoginPage
from selenium_project.pages.dropdown import DropDownPage
from selenium_project.pages.date_picker import DatePicker
from selenium_project.pages.file_upload import FileUpload
from selenium_project.pages.slider import Slider


TARGET_URL = "https://www.selenium.dev/selenium/web/web-form.html"


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests against"
    )


@pytest.fixture
def browser(request) -> str:
    return request.config.getoption("--browser")

@pytest.fixture
def driver(browser):
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=ChromeService())
        driver.implicitly_wait(60)
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
        driver.implicitly_wait(60)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.get(TARGET_URL)
    yield driver
    driver.quit()

@pytest.fixture
def slider(driver) -> Slider:
    return Slider(driver)

@pytest.fixture
def dropdown_page(driver) -> DropDownPage:
    return DropDownPage(driver)

@pytest.fixture
def file_upload(driver) -> FileUpload:
    return FileUpload(driver)

@pytest.fixture
def date_picker(driver) -> DatePicker:
    driver.refresh()
    return DatePicker(driver)

@fixture
def login_page()-> Generator[LoginPage, Any, None]:
    """This fixture returns a WebDriver."""
    logging.debug("Initializing Chrome WebDriver")
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(TARGET_URL)
    login = LoginPage(chrome_driver)
    logging.debug("Starting test execution")
    yield login
    chrome_driver.close()

@fixture(
    params=['Jan', 'Feb', 'Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ids=lambda c: c)
def month(request):
    """, 'Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'"""
    return request.param
