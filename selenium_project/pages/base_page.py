import logging
from typing import Tuple
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium_project.locators.locators import Locator


class BasePage:
    """Page Object for BasePage functionality."""
    def __init__(self,driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=timeout)

    def launch_web_driver(self, target_url: str) -> None:
        """Navigate to the target URL and wait until DOM is available."""
        self.driver.get(target_url)
        try:
            self.wait_present(Locator.body_element)
        except TimeoutException as err:
            logging.error("Page loading failed", exc_info=True)
            raise RuntimeError("Page loading failed") from err

    def wait_visible(self, locator: Tuple[str, str]) -> WebElement:
        """Wait until element is visible."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator: Tuple[str, str]) -> WebElement:
        """Wait until element is clickable."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_present(self, locator: Tuple[str, str]) -> WebElement:
        """Wait until element is present."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_not_visible(self, locator: Tuple[str, str]) -> WebElement:
        """Wait until element is invisible."""
        return self.wait.until(EC.invisibility_of_element(locator))

    def is_element_visible(self, locator:Tuple[str, str]) -> bool:
        """Return True if element is displayed, else False."""
        return self.wait_visible(locator).is_displayed()

    def submission_success(self)-> bool:
        """Verify submission success."""
        message = self.wait_visible(Locator.submission_success)
        return message.is_displayed()

    def click_element(self, locator: Tuple[str, str]) -> None:
        """Click element and retry if it becomes stale."""
        def _click(driver):
            try:
                element = driver.find_element(*locator)
                element.click()
                return True
            except StaleElementReferenceException:
                return False
        self.wait.until(_click)

    @staticmethod
    def send_control_keys(element: WebElement, value:str) -> None:
        """Tap Control key + given value."""
        element.send_keys(Keys.CONTROL, value)

    @staticmethod
    def tap_backspace(element: WebElement) -> None:
        """Tap backspace."""
        element.send_keys(Keys.BACKSPACE)