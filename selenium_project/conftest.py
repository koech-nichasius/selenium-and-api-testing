import logging
import pytest
from pytest import fixture
from selenium import webdriver
from typing import Iterable, TypeVar


from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from Selenium.pages import LoginPage
from Selenium.pages.login import LoginPage
from Selenium.pages.dropdown import DropDownPage
from Selenium.pages.date_picker import DatePicker
from Selenium.pages.file_upload import FileUpload

from Selenium.pages.slider import Slider

T=TypeVar("T")
TARGET_URL = "https://www.selenium.dev/selenium/web/web-form.html"
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Select the browser to use in test."
    )


@pytest.fixture
def browser(request)-> str:
    return request.config.getoption("--browser")

@pytest.fixture(scope="function")
def driver(browser):
    if browser == "chrome":
        selected_driver = webdriver.Chrome(service=ChromeService())
    elif browser == "firefox":
        selected_driver = webdriver.Firefox(service=FirefoxService())
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    selected_driver.get(TARGET_URL)
    yield selected_driver
    selected_driver.quit()

@pytest.fixture
def slider(driver) -> Slider:
    return Slider(driver)

@pytest.fixture
def dropdown_page(driver) -> DropDownPage:
    return DropDownPage(driver)

@pytest.fixture(scope="function")
def file_upload(driver) -> FileUpload:
    return FileUpload(driver)

@pytest.fixture
def date_picker(driver) -> DatePicker:
    driver.refresh()
    return DatePicker(driver)

# @pytest.fixture
# def login_page(driver) -> Generator[LoginPage, Any, None]:
#     # driver.refresh()
#     yield LoginPage(driver)
#     driver.close()

@fixture
def login_page()-> Iterable[T]:
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
