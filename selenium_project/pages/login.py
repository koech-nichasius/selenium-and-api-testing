from selenium.webdriver.support import expected_conditions as EC
from selenium_project.config import BASE_URL
from selenium_project.pages.base_page import BasePage
from selenium_project.locators.locators import Locator


class LoginPage(BasePage):
    """"This class contains functions for the Login Functionality"""
    def __init__(self, driver):
        super().__init__(driver)
        self.launch_web_driver(BASE_URL)

    def enter_user_name(self, user_name:str)-> None:
        """Enter the User Login  Name."""
        user_name_field=self.driver.find_element(
            *Locator.user_name_input
        )
        user_name_field.clear()
        user_name_field.send_keys(user_name)

    def enter_password(self, password:str)-> None:
        """Enter the User Login Password."""
        password_field=self.driver.find_element(
            *Locator.password_input
        )
        password_field.clear()
        password_field.send_keys(password)

    def tap_login_btn(self)-> None:
        """Press Login Button"""
        self.wait.until(
            EC.element_to_be_clickable(
                Locator.submit_button
            )
        ).click()

    def is_logged_in(self)-> bool:
        """Verify Login successful window opened."""
        self.wait.until(
            lambda d: Locator.submission_form in d.current_url
        )
        return  Locator.submission_form in self.driver.current_url


