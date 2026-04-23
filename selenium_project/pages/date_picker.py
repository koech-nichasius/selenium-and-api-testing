from typing import List
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium_project.common_functions.common_functions import Common
from selenium_project.test_data.locators import Locator
from selenium_project.test_data.test_data import TestData


class DatePicker(Common):
    """Page Object for DatePicker functionality."""

    def __init__(self, driver):
        super().__init__(driver)
        self.load_page(TestData.base_url)

    @property
    def month_switch(self):
        """Returns the month switch element"""
        return self.driver.find_element(*Locator.month_switch)

    @property
    def next_month(self):
        """Returns the next element"""
        return self.driver.find_element(*Locator.next_month)

    @property
    def prev_month(self):
        """Returns the prev element"""
        return self.driver.find_element(*Locator.prev_month)

    @property
    def date_input(self) -> WebElement:
        """Returns the Date Field element."""
        return self.wait_clickable(Locator.date_input)

    def clear_existing_date(self) -> None:
        """"Clear date field."""
        self.date_input.clear()

    def tap_date_field(self) -> None:
        """Tap Date input field."""
        self.date_input.click()

    def is_calendar_displayed(self) -> bool:
        """Return True if Calendar is displayed, else False."""
        return self.is_element_visible(Locator.month_switch)

    def tap_month_switch(self)-> None:
        """Tap on Month switch menu"""
        self.month_switch.click()

    def tap_next_icon(self)-> None:
        """Tap on Next icon."""
        self.next_month.click()

    def tap_prev_icon(self)-> None:
        """Tap on Prev icon."""
        self.prev_month.click()

    def navigate_to_next_month(self,target_month)-> None:
        """Navigate to specified month via date picker switch."""
        while True:
            header = self.driver.find_element(*Locator.month_switch).text
            if header.startswith(target_month):
                break
            self.tap_next_icon()

    def select_month(self, month_name: str) -> None:
        """
        Clicks a visible element like <span class="month">May</span> that equals the given month_name.
        """
        self.tap_month_switch()
        self.wait_clickable(
            (By.XPATH, f"//span[contains(@class,'month') and normalize-space(text())='{month_name}']")
        ).click()


    def get_all_months(self)-> list[WebElement]:
        """Return a list of all months in Calendar."""
        self.tap_month_switch()
        return self.driver.find_elements(*Locator.all_months)

    def get_dates(self) -> List[WebElement] :
        """Get available dates for a selected month."""
        return self.driver.find_elements(*Locator.all_dates)

    def select_date(self, date_val: int) -> None:
        """Select a given calendar date. Hanles stale elements in case of refresh."""
        xpath = f"//td[contains(@class,'day') and normalize-space()='{date_val}']"
        for _ in range(3):
            try:
                self.wait_clickable((By.XPATH, xpath)).click()
                return
            except StaleElementReferenceException:
                continue
        raise AssertionError(f"Date {date_val} could not be selected")

    def verify_date_set(self, date_set: int) -> bool:
        """Verify thet the selected date is set."""
        return int(self.date_input.get_attribute("value").split("/")[1]) == date_set

    def verify_month_selected(self, month: str) -> bool:
        """Verify thet the selected month is set."""
        return month in self.month_switch.text
