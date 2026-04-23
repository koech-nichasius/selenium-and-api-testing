class Slider(Common):
    """Page Object for Slider functionality."""

    def __init__(self, driver):
        super().__init__(driver)

    def open(self) -> None:
        self.load_page(TestData.base_url)

    @property
    def slider(self) -> WebElement:
        return self.driver.find_element(By.NAME, Locator.slider)

    def set_slider_value(self, value: int) -> None:
        min_val = self.get_slider_min_value()
        max_val = self.get_slider_max_value()

        if not min_val <= value <= max_val:
            raise ValueError(f"Value {value} out of range ({min_val}-{max_val})")

        self.driver.execute_script(
            """
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            """,
            self.slider,
            value
        )

    def get_slider_min_value(self) -> int:
        return int(self.slider.get_attribute("min"))

    def get_slider_max_value(self) -> int:
        return int(self.slider.get_attribute("max"))

    def get_slider_value(self) -> int:
        return int(self.slider.get_attribute("value"))