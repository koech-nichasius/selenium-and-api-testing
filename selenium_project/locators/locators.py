from dataclasses import dataclass

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

@dataclass
class Locator:
    """This dataclass contains locator names."""

    user_name_box: str = '//input[@id="my-text-id"]'
    password_box: str = 'input[type="password"]'
    submit_button: str = "button"
    disabled_input: str = "my-disabled"

    # Dropdown
    dropdown_select: WebElement = 'input[name="my-select"]'
    file_btn: WebElement = '"my-file"'
    submission_success = "https://www.selenium.dev/selenium/web/submitted-form.html"

    # Slider
    slider:str = "my-range"


