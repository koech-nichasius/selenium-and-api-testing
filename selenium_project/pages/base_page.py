import logging
from typing import Tuple
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

LocatorType = Tuple[str, str]

class BasePage:
    """Base class for all Page Objects."""

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def load_page(self, url: str) -> None:
        """Navigate to URL and wait until DOM is loaded."""
        self.driver.get(url)
        try:
            self.wait_present(("tag name", "body"))
        except TimeoutException as err:
            logging.error("Page load failed", exc_info=True)
            raise RuntimeError(f"Failed to load page: {url}") from err

    def wait_present(self, locator: LocatorType) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_visible(self, locator: LocatorType) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator: LocatorType) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_not_visible(self, locator: LocatorType) ->  WebElement:
        kk = self.wait.until(EC.invisibility_of_element_located(locator))
        return kk

    def click(self, locator: LocatorType) -> None:
        """Click element safely."""
        self.wait_clickable(locator).click()

    def is_element_visible(self, locator: LocatorType) -> bool:
        """Return True if element is displayed, else False."""
        try:
            return self.wait_visible(locator).is_displayed()
        except TimeoutException:
            return False

    def is_element_present(self, locator: LocatorType) -> bool:
        """Return True if element is present, else False."""
        try:
            self.wait_present(locator)
            return True
        except TimeoutException:
            return False

    @staticmethod
    def send_control_keys(element: WebElement, value: str) -> None:
        element.send_keys(Keys.CONTROL, value)

    @staticmethod
    def tap_backspace(element: WebElement) -> None:
        element.send_keys(Keys.BACKSPACE)
