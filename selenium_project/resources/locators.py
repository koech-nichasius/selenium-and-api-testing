from typing import Tuple
from dataclasses import dataclass
from selenium.webdriver.common.by import By

LocatorType = Tuple[str, str]

def by_xpath(element: str) -> LocatorType:
    """Find element by XPATH."""
    return By.XPATH, f"{element}"

def by_id(element: str) -> LocatorType:
    """Find element by ID."""
    return By.ID, f"{element}"

def by_name(element: str) -> LocatorType:
    """Find element by NAME."""
    return By.NAME, f"{element}"

def by_tag_name(element: str) -> LocatorType:
    """Find element by TAG NAME."""
    return By.TAG_NAME, f"{element}"

def by_css(element: str) -> LocatorType:
    """Find element by CSS_SELECTOR."""
    return By.CSS_SELECTOR, f"{element}"

@dataclass
class CommonLocator:
    """This dataclass common contains locators."""
    # Login elements
    user_name_input = by_name('my-text')
    password_input =  by_name("my-password")
    submit_button = by_xpath("//button[@type='submit']")
    disabled_input = by_name("my-disabled")
    read_only_input = by_name("my-read-only")

    # Dropdown elements
    dropdown_select = by_name("my-select")

    # Submission page
    submission_success = by_id("message")
    submission_form = "submitted-form.html"

    # File Upload elements
    file_upload: str = by_name("my-file")

    # Slider elements
    slider:str = "my-range"

    # Calendar elements
    all_dates = by_xpath(
        "//td[contains(@class,'day') "
        "and not(contains(@class,'old')) "
        "and not(contains(@class,'active')) "
        "and not(contains(@class,'new'))]"
    )
    date_input = by_name("my-date")
    next_month = by_xpath("//th[@class='next']")
    prev_month = by_xpath("//th[@class='prev']")
    month_switch = by_css("th[class='datepicker-switch']")
    all_months = by_xpath(
        "//span[contains(concat(' ', "
        "normalize-space(@class), ' '), ' month ')]")

    @staticmethod
    def month_by_name(month_name: str) -> LocatorType:
        return by_xpath(
            f"//span[contains(@class,'month') "
            f"and normalize-space(text())='{month_name}']")

    @staticmethod
    def date_by_value(date_val: int) -> LocatorType:
        return by_xpath(
            f"//td[contains(@class,'day') "
            f"and normalize-space()='{date_val}']")

@dataclass
class WebTableLocator:
    """This dataclass contains Web Table locators."""
    table = by_xpath("//form//table")
    table_headers = by_xpath(".//tr/th")
    table_rows = by_xpath(".//tbody/tr")
    row_cells = by_tag_name("td")


