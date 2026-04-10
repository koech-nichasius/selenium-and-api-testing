from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_project.interfaces.driver import IBasePage
from selenium_project.locators.locators import Locator


class LoginPage(IBasePage):
    """"This class represents functions for the Login Page"""
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open_login_page(self, url:str)-> None:
        self.driver.get(url)

    def is_login_success(self)-> bool:
        """Verify login success."""
        WebDriverWait(self.driver, 5).until(
            lambda d: d.current_url.startswith(
                Locator.submission_success
            )
        )
        return self.driver.current_url.startswith(
            Locator.submission_success
        )

    def enter_user_name(self, user_name:str)-> None:
        """Enter the User Login  Name."""
        user_name_field=self.driver.find_element(
            By.XPATH,'//input[@id="my-text-id"]'
        )
        user_name_field.clear()
        user_name_field.send_keys(user_name)

    def enter_password(self, password:str)-> None:
        """Enter the User Login Password."""
        password_field=self.driver.find_element(
            By.NAME,Locator.password_box
        )
        password_field.clear()
        password_field.send_keys(password)

    def tap_login_btn(self)-> None:
        """Press Login Button"""
        submit_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, Locator.submit_button)
            )
        )
        submit_button.click()

    def is_logged_in(self)-> bool:
        """Verify Login successful window opened."""
        self.wait.until(
            lambda d: d.current_url.startswith(
                Locator.submission_success
            )
        )
        return self.driver.current_url.startswith(Locator.submission_success)

