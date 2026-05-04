import random
from typing import Generator, Any
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_project.resources.selenium_data import SeleniumData
from selenium_project.pages.login import LoginPage
from selenium_project.pages.dropdown import DropDownPage
from selenium_project.pages.date_picker import DatePicker
from selenium_project.pages.file_upload import FileUpload
from selenium_project.pages.slider import Slider
from selenium_project.pages.web_table import WebTable


def pytest_addoption(parser):
    parser.addoption(
        "--on-browser",
        action="store",
        default="chrome",
        help="Browser to run tests against"
    )


@fixture
def browser(request) -> str:
    """Get terminal option for which browser to use."""
    return request.config.getoption("--on-browser")

@fixture
def driver(browser) -> Generator[WebDriver | WebDriver, Any, None]:
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
def slider(driver :WebDriver) -> Slider:
    """Instantiate Slider class."""
    return Slider(driver)

@fixture
def drop_down(driver :WebDriver) -> DropDownPage:
    """Instantiate DropDownPage class."""
    return DropDownPage(driver)

@fixture
def file_upload(driver :WebDriver) -> FileUpload:
    """Instantiate FileUpload class."""
    return FileUpload(driver)

@fixture
def date_picker(driver :WebDriver) -> DatePicker:
    """Instantiate DatePicker class."""
    return DatePicker(driver)

@fixture
def web_table(driver :WebDriver) -> WebTable:
    """Instantiate WebTable class."""
    return WebTable(driver)

@fixture
def login(driver :WebDriver) -> LoginPage:
    """Instantiate LoginPage class."""
    return LoginPage(driver)

@fixture(params=SeleniumData.calendar_months, ids=lambda c: c)
def months(request) -> str:
    """Fixture returns Calendar months one at a time.'"""
    return request.param

@fixture()
def all_calendar_months() -> str:
    """Fixture returns Calendar months.'"""
    return SeleniumData.calendar_months

@fixture
def random_months(all_calendar_months :str) -> list[str]:
    """Fixture returns 5 Calendar months one at a time.'"""
    random_months = 5
    return random.sample(all_calendar_months, random_months)
