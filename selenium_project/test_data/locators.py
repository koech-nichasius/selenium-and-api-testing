from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class Locator:
    """This dataclass contains locator names."""
    body_element = (By.TAG_NAME, "body")
    # Login elements
    user_name_input = (By.NAME, 'my-text')
    password_input =  (By.NAME, "my-password")
    submit_button = (By.XPATH, "//button[@type='submit']")
    disabled_input = (By.NAME, "my-disabled")
    read_only_input = (By.NAME, "my-read-only")

    # Dropdown elements
    dropdown_select = (By.NAME, "my-select")

    # Submission page
    submission_success = (By.ID, "message")
    submission_form = "submitted-form.html"

    # File Upload elements
    file_upload: str = (By.NAME, "my-file")

    # Slider elements
    slider:str = "my-range"

    # Calendar elements
    all_dates = (
        By.XPATH,
        "//td[contains(@class,'day') "
        "and not(contains(@class,'old')) "
        "and not(contains(@class,'active')) "
        "and not(contains(@class,'new'))]"
    )
    date_input = (By.NAME, "my-date")
    next_month = (By.XPATH, "//th[@class='next']")
    prev_month = (By.XPATH, "//th[@class='prev']")
    month_switch = (By.CSS_SELECTOR, "th[class='datepicker-switch']")
    all_months = (By.XPATH, "//span[contains(concat(' ', normalize-space(@class), ' '), ' month ')]")

    @staticmethod
    def month_by_name(month_name: str):
        return (By.XPATH,
            f"//span[contains(@class,'month') and normalize-space(text())='{month_name}']")

    @staticmethod
    def date_by_value(date_val: int):
        return (By.XPATH,
            f"//td[contains(@class,'day') and normalize-space()='{date_val}']")

    # Web Table elements
    table = (By.XPATH,"//form//table")
    table_headers = (By.XPATH, ".//tr/th")
    table_rows = (By.XPATH, ".//tbody/tr")
    row_cells = (By.TAG_NAME, "td")


