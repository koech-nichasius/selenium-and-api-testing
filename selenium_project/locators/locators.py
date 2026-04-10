from dataclasses import dataclass

@dataclass
class Locator:
    """This dataclass contains locator names."""
    user_name_box: str = '//input[@id="my-text-id"]'
    password_box: str =  "my-password"
    submit_button: str = "//button[normalize-space()='Submit']"
    disabled_input: str = "my-disabled"

    # Dropdown
    dropdown_select: str = 'input[name="my-select"]'
    file_btn: str = '"my-file"'
    submission_success: str = "https://www.selenium.dev/selenium/web/submitted-form.html"

    # File Upload
    file_upload: str = "my-file"

    # Slider
    slider:str = "my-range"


