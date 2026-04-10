from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Selenium.interfaces.driver import ILoginPage
from Selenium.locators.locators import Locator


class LoginPage(ILoginPage):
    """"This class represents functions for the Login Page"""
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self, url:str)-> None:
        self.driver.get(url)

    def is_login_success(self)-> bool:
        """Verify login success."""
        WebDriverWait(self.driver, 5).until(lambda d: d.current_url.startswith(Locator.submission_success))
        return self.driver.current_url.startswith(Locator.submission_success)

    def enter_user_name(self, user_name:str)-> None:
        """Enter the User Login  Name."""
        user_name_field=self.driver.find_element(By.XPATH,'//input[@id="my-text-id"]')
        user_name_field.clear()
        user_name_field.send_keys(user_name)

    def enter_password(self, password:str)-> None:
        """Enter the User Login Password."""
        password_field=self.driver.find_element(By.CSS_SELECTOR,Locator.password_box)
        password_field.clear()
        password_field.send_keys(password)

    def tap_login_btn(self)-> None:
        """Press Login Button"""
        self.driver.find_element(By.CSS_SELECTOR, Locator.submit_button).click()

    def is_logged_in(self)-> bool:
        """Verify Login successful window opened."""
        WebDriverWait(self.driver, 5).until(lambda d: d.current_url.startswith(Locator.submission_success))
        return self.driver.current_url.startswith(Locator.submission_success)

