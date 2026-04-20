from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium_project.config import BASE_URL
from selenium_project.pages.base_page import BasePage
from selenium_project.locators.locators import Locator


class Slider(BasePage):
    """Page Object for Slider functionality."""

    def __init__(self, driver):
        super().__init__(driver)
        self.launch_web_driver(BASE_URL)

    @property
    def slider(self) -> WebElement:
        """Slider WebElement."""
        return self.driver.find_element(By.NAME, Locator.slider)

    def set_slider_value(self, value: int)-> None:
        """Set actual slider value. Move the slider {offset} pixels to the right"""
        self.driver.execute_script(
            """
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input'));
            arguments[0].dispatchEvent(new Event('change'));
            """,
            self.slider,
            value )

    def get_slider_min_value(self)-> int:
        """Get slider min value."""
        return int(self.slider.get_attribute("min"))

    def get_slider_max_value(self)-> int:
        """Get slider max value."""
        return int(self.slider.get_attribute("max"))

    def get_slider_value(self)-> int:
        """Get slider default value."""
        curr_slider_val:int=int(self.slider.get_attribute("value"))
        return curr_slider_val