import json
import time
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/webtables.php")
wait= WebDriverWait(driver, 10)
# wait.until(EC.element_to_be_clickable(edit_btns[2])).click()
time.sleep(5)

table =  driver.find_element(By.XPATH,"//form//table")
t_headers= table.find_elements(By.XPATH, ".//tr/th")
t_rows = table.find_elements(By.XPATH, ".//tbody/tr")

edit_btns = table.find_elements(By.XPATH, ".//tbody/tr")



table_headers = [th.text.strip() for th in t_headers]

@pytest.fixture
def json_file_path():
    json_path = (
            Path(__file__).resolve()
            .parent.parent
            / "data"
            / "table_output.json"
    )
    return json_path

def test_table_data(json_file_path):
    json_data = []

    for row in t_rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        cell_values = [cell.text.strip() or None for cell in cells]

        # Skip rows that don't match header length
        if len(cell_values) != len(table_headers):
            print(f"Skipping row: {cell_values}")
            continue

        row_dict = dict(zip(table_headers, cell_values))
        json_data.append(row_dict)


def test_json_file_exists(json_file_path):
    assert json_file_path.exists(), "JSON output file was not created"


def test_json_is_valid(json_file_path):
    with json_file_path.open(encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list), "JSON root should be a list"


def test_json_not_empty(json_file_path):
    with json_file_path.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) > 0, "JSON file contains no table rows"


def test_json_row_structure(json_file_path):
    with json_file_path.open(encoding="utf-8") as f:
        data = json.load(f)

    first_row = data[0]

    assert isinstance(first_row, dict), "Each table row must be a dict"


def test_json_headers_match_expected(json_file_path):
    expected_headers = {
        'Last Name',
         'Age',
         'Action',
         'Email',
         'First Name',
         'Department',
         'Salary'
    }

    with json_file_path.open(encoding="utf-8") as f:
        data = json.load(f)

    actual_headers = set(data[0].keys())
    assert actual_headers == expected_headers, (
        f"Expected headers {expected_headers}, got {actual_headers}"
    )


def test_no_empty_cell_values(json_file_path):
    with json_file_path.open(encoding="utf-8") as f:
        data = json.load(f)
    for row in data:
        assert row["Action"] is None

        for key, value in row.items():
            assert value not in ("", None), (
                f"Empty value found for key '{key}'"
            )
