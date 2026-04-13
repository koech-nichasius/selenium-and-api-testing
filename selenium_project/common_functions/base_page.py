from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from selenium_project.locators.locators import Locator

SUBMIT_SUCCESS = "https://www.selenium.dev/selenium/web/submitted-form.html"

class BasePage:
    """This class represents functions for the Login Page"""
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @staticmethod
    def send_control_keys(element: WebElement, value:str) -> None:
        """Select all pre-existing values."""
        element.send_keys(Keys.CONTROL, value)

    @staticmethod
    def tap_backspace(element: WebElement) -> None:
        """Tap backspace."""
        element.send_keys(Keys.BACKSPACE)

    def wait_until_element_visible(self, widget) -> None:
        """Wait until element is vivible."""
        self.wait.until(EC.visibility_of_element_located(widget))

    def is_element_visible(self,element) -> bool:
        """Return True if element is displayed, else False."""
        return self.wait.until(EC.visibility_of_element_located(element)).is_displayed()

    def submission_success(self)-> bool:
        """Verify login success."""
        message = self.wait.until(
            EC.visibility_of_element_located(
                Locator.submission_success
            )
        )
        return message.is_displayed()

    def click_element(self,element):
        """Function handles stale elements. Fresh element look-upo is initiated incase it is stale."""
        try:
            element.click()
        except StaleElementReferenceException:
            element = self.driver.find_element(*element)
            element.click()
