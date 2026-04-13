from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_project.interfaces.base_page import BasePage
from selenium_project.locators.locators import Locator


class FileUpload(BasePage):
    """"This class represents functions for the File Upload Functionality in Base Page."""
    def __init__(self, driver):
        super().__init__(driver)
        self.wait=WebDriverWait(self.driver, 10)

    @property
    def file_upload(self) -> WebElement:
        return self.driver.find_element(By.NAME, Locator.file_upload)

    def upload_file(self, file_path:str)-> None:
        """Upload file"""
        path = Path(file_path)
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {path}")
        self.file_upload.send_keys(file_path)

    def get_uploaded_file(self)-> str:
        """Get uploaded file"""
        return self.file_upload.get_attribute("value")

    def tap_submit_btn(self)-> None:
        """Press submit Button"""
        self.driver.find_element(*Locator.submit_button).click()

    def is_file_submitted(self) -> bool:
        """Verify submission successful window opened."""
        message = self.wait.until(
            EC.visibility_of_element_located(
                Locator.submission_success
            )
        )
        return message.is_displayed()
