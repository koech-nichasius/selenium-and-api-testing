from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class Locator:
    """This dataclass contains locator names."""
    # Login elements
    user_name_input = (By.NAME, 'my-text')
    password_input =  (By.NAME, "my-password")
    submit_button = (By.XPATH, "//button[@type='submit']")
    disabled_input = (By.NAME, "my-disabled")
    read_only_input = (By.NAME, "my-read-only")

    # Dropdown
    dropdown_select: str = 'input[name="my-select"]'
    file_btn: str = '"my-file"'

    # Submission page
    submission_success = (By.ID, "message")
    submission_form = "submitted-form.html"

    # File Upload
    file_upload: str = "my-file"

    # Slider
    slider:str = "my-range"

    # Calendar elements
    all_dates = (By.XPATH, "//td[contains(@class, 'day')]")
    date_input = (By.CSS_SELECTOR, 'input[name="my-date"]')
    all_months = (By.XPATH, "//span[contains(concat(' ', normalize-space(@class), ' '), ' month ')]")
    month_switch = (By.CSS_SELECTOR, 'th[class="datepicker-switch"]')


