from abc import ABC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class ILoginPage(ABC):
    """This class represents functions for the Login Page"""
    def __init__(self,driver):
        self.driver = driver

    @staticmethod
    def send_control_keys(element: WebElement, value:str):
        """Select all pre-existing values."""
        element.send_keys(Keys.CONTROL, value)

    @staticmethod
    def tap_backspace(element: WebElement):
        """Tap backspace."""
        element.send_keys(Keys.BACKSPACE)