import json
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("https://www.tutorialspoint.com/selenium/practice/webtables.php")
# wait= WebDriverWait(driver, 10)
# time.sleep(5)
#
# table =  driver.find_element(By.XPATH,"//form//table")
# t_headers= table.find_elements(By.XPATH, ".//tr/th")
# t_rows = table.find_elements(By.XPATH, ".//tbody/tr")
#
# edit_btns = table.find_elements(By.XPATH, ".//tbody/tr")
# # wait.until(EC.element_to_be_clickable(edit_btns[2])).click()
#
#
# table_headers = [th.text.strip() for th in t_headers]
#
# json_data = []
#
# for row in t_rows:
#     cells = row.find_elements(By.TAG_NAME, "td")
#     cell_values = [cell.text.strip() or None for cell in cells]
#
#     # Skip rows that don't match header length
#     if len(cell_values) != len(table_headers):
#         print(f"Skipping row: {cell_values}")
#         continue
#
#     row_dict = dict(zip(table_headers, cell_values))
#     json_data.append(row_dict)


# write to file
output_file = Path("../data/table_output.json")
with output_file.open("w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)


# for row_index, row in enumerate(rows, start=1):
#     cells = row.find_elements(By.TAG_NAME, "td")
#     row_data = [cell.text for cell in cells]
#     print(f"Row {row_index}: {row_data}")
#
#     if "Cierra" in row.text:
#         row.find_element(
#             By.XPATH, ".//a[contains(@class,'edit-wrap')]"
#         ).click()
#
#     time.sleep(30)

