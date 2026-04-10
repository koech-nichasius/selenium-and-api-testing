from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from selenium_project.interfaces.driver import ILoginPage
from selenium_project.locators.locators import Locator


class FileUpload(ILoginPage):
    """"This class represents functions for the Login Page"""
    def __init__(self, driver):
        super().__init__(driver)
        self._file_upload : WebElement = self.driver.find_element(By.CSS_SELECTOR, 'input[name="my-file"]')

    

    def upload_file(self, file_2_upload)-> None:
        """Upload file"""
        self._file_upload.send_keys(file_2_upload)

    def get_uploaded_file(self)-> str:
        """Get uploaded file"""
        return self._file_upload.get_attribute("value")

    def tap_submit_btn(self)-> None:
        """Press submit Button"""
        self.driver.find_element(By.CSS_SELECTOR, Locator.submit_button).click()

    def is_file_submitted(self) -> bool:
        """Verify Login successful window opened."""
        WebDriverWait(self.driver, 5).until(lambda d: d.current_url.startswith(Locator.submission_success))
        return self.driver.current_url.startswith(Locator.submission_success)
