from typing import List
from selenium.webdriver.common.by import By

from selenium_project.locators.locators import Locator

TARGET_URL="https://www.tutorialspoint.com/selenium/practice/webtables.php"

class WebTable:
    """"This class represents functions for the Web Table Page"""

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TARGET_URL)

    @property
    def table(self):
        """Returns table web element."""
        return self.driver.find_element(*Locator.table)

    def get_table_headers(self) -> List[str]:
        """Return table headers."""
        table_headers: List[str] = [
            th.text.strip() for th in self.table.find_elements(*Locator.table_headers)]
        return table_headers

    def get_table_rows(self):
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
        # wait.until(EC.element_to_be_clickable(edit_btns[2])).click()
        ...