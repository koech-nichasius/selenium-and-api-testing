from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium_project.config import WEB_TABLE_URL
from selenium_project.locators.locators import Locator
from selenium_project.pages.base_page import BasePage

class WebTable(BasePage):
    """"This class contains functions for the Web Table Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.launch_web_driver(WEB_TABLE_URL)

    @property
    def table(self) -> WebElement:
        """Returns table web element."""
        return self.driver.find_element(*Locator.table)

    def get_table_headers(self) -> List[str]:
        """Return table headers."""
        table_headers: List[str] = [
            th.text.strip() for th in self.table.find_elements(*Locator.table_headers)]
        return table_headers

    def get_table_rows(self) -> List[dict]:
        """Return table rows values mapped to table headers-."""
        headers = self.get_table_headers()
        rows=self.table.find_elements(*Locator.table_rows)
        table_rows=[]
        for row in rows:
            cells = row.find_elements(*Locator.row_cells)
            row_values = [cell.text.strip() for cell in cells]
            if not row_values:
                # Skip empty rows
                continue
            table_rows.append(dict(zip(headers, row_values)))
        return table_rows

    def add_table_record(self):
        # self.wait_clickable(edit_btns[2]).click()
        ...