from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_project.interfaces.driver import IBasePage
from selenium_project.locators.locators import Locator


class FileUpload(IBasePage):
    """"This class represents functions for the File Upload Functionality in Base Page."""
    def __init__(self, driver):
        super().__init__(driver)

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
        self.driver.find_element(By.CSS_SELECTOR, Locator.submit_button).click()

    def is_file_submitted(self) -> bool:
        """Verify Login successful window opened."""
        # WebDriverWait(self.driver, 5).until(lambda d: d.current_url.startswith(Locator.submission_success))

        WebDriverWait(self.driver, 5).until(
            EC.url_contains(Locator.submission_success)
        )

        return self.driver.current_url.startswith(Locator.submission_success)
