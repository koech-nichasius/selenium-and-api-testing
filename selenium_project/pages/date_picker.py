from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from selenium_project.common_functions.base_page import BasePage
from selenium_project.locators.locators import Locator


class DatePicker(BasePage):
    """"This class represents functions for the Login Page"""

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def date_input(self) -> WebElement:
        """Click on the Date Field"""
        return self.driver.find_element(*Locator.date_input)

    def clear_existing_date(self) -> None:
        """"Clear date field."""
        date_input:WebElement =self.driver.find_element(self.date_input)
        date_input.click()
        self.send_control_keys(self.driver.find_element(date_input), "a")
        self.tap_backspace(date_input)

    def clear_entire_text(self) -> None:
        date_input=self.driver.find_element(self.date_input)
        date_input.date_input.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

    def tap_date_field(self) -> None:
        """Tap Date input field."""
        self.wait.until(EC.element_to_be_clickable(Locator.date_input)).click()

    def is_calendar_displayed(self) -> bool:
        """Return True if Calendar is displayed, else False."""
        return self.is_element_visible(Locator.month_switch)

    def tap_month_switch(self)-> None:
        """Tap on Month switch menu"""
        self.wait.until(EC.visibility_of_element_located(Locator.month_switch)).click()

    def select_month(self, month_name: str) -> None:
        """
        Clicks a visible element like <span class="month">May</span> that equals the given month_name.
        """
        self.tap_month_switch()
        month_el = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[contains(@class,'month') and normalize-space(text())='{month_name}']")))
        month_el.click()

    def get_all_months(self)-> list[WebElement]:
        """Return a list of all months in Calendar."""
        self.tap_month_switch()

        all_months: List[WebElement] =self.driver.find_elements(*Locator.all_months)
        return all_months

    def get_dates(self) -> List[WebElement] :
        """Get available dates for a selected month."""
        "data-date"
        return self.driver.find_elements(*Locator.all_dates)

    def select_date(self, date_val: int) -> None:
        """Select date."""
        date = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//td[contains(@class,'day') and normalize-space(.)='{str(date_val)}']")))
        date.click()

    def verify_date_set(self, date_set: int) -> bool:
        """Verify thet the selected date is set."""
        return int(self.date_input.get_attribute("value").split("/")[1]) == date_set

