import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium_project.locators.locators import Locator

class BasePage:
    """This class contains common functions."""
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def launch_web_driver(self, target_url: str) -> None:
        """Navigate to the target URL and ensure browser session is available."""
        self.driver.get(target_url)

        try:
            self.wait.until(self.is_browser_launched)
        except TimeoutException as err:
            logging.error("Browser launching failed", exc_info=True)
            raise RuntimeError("Browser launching failed") from err

    def is_browser_launched(self, driver) -> bool:
        """Check that the browser is launched."""
        return self.driver.session_id and self.driver.window_handles

    @staticmethod
    def send_control_keys(element: WebElement, value:str) -> None:
        """Tap Control key + given value."""
        element.send_keys(Keys.CONTROL, value)

    @staticmethod
    def tap_backspace(element: WebElement) -> None:
        """Tap backspace."""
        element.send_keys(Keys.BACKSPACE)

    def wait_until_element_visible(self, element) -> None:
        """Wait until element is visible."""
        self.wait.until(EC.visibility_of_element_located(element))

    def is_element_visible(self,element) -> bool:
        """Return True if element is displayed, else False."""
        return self.wait.until(
            EC.visibility_of_element_located(element)).is_displayed()

    def submission_success(self)-> bool:
        """Verify submission success."""
        message = self.wait.until(
            EC.visibility_of_element_located(Locator.submission_success))
        return message.is_displayed()

    def click_element(self,element):
        """Function handles stale elements. Fresh element
        look-upo is initiated incase it is stale."""
        try:
            element.click()
        except StaleElementReferenceException:
            element = self.driver.find_element(*element)
            element.click()
