from dataclasses import dataclass


@dataclass
class SeleniumData:
    """This dataclass contains Test data."""
    base_url = "https://www.selenium.dev/selenium/web/web-form.html"
    web_table_url = "https://www.tutorialspoint.com/selenium/practice/webtables.php"
    submission_success = "https://www.selenium.dev/selenium/web/submitted-form.html"
    calendar_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Slider data
    slider_min_value = 0
    slider_max_value = 10
    slider_default_value = 5