from selenium.webdriver.remote.webelement import WebElement
from selenium_project.config import BASE_URL
from selenium_project.pages.base_page import BasePage
from selenium_project.locators.locators import Locator


class LoginPage(BasePage):
    """Page Object for Login functionality."""
    def __init__(self, driver):
        super().__init__(driver)
        self.load_page(BASE_URL)

    @property
    def user_name_field(self) -> WebElement:
        """Function returns the username field element."""
        return self.driver.find_element(*Locator.user_name_input)

    @property
    def password_field(self) -> WebElement:
        """Function returns the password field element."""
        return self.driver.find_element(*Locator.password_input)

    @property
    def submit_button(self) -> WebElement:
        """Function returns the submit button element."""
        return self.wait_clickable(Locator.submit_button)

    def enter_user_name(self, user_name:str) -> None:
        """Enter the User Login  Name."""
        self.user_name_field.clear()
        self.user_name_field.send_keys(user_name)

    def enter_password(self, password:str)-> None:
        """Enter the User Login Password."""
        self.password_field.clear()
        self.password_field.send_keys(password)

    def tap_login_btn(self)-> None:
        """Press Login Button"""
        self.submit_button.click()

    def is_logged_in(self)-> bool:
        """Verify Login successful window opened."""
        self.wait.until(lambda d: Locator.submission_form in d.current_url)
        return  Locator.submission_form in self.driver.current_url


