import random
import pytest
from selenium_project.config import CALENDAR_MONTHS


class TestDatePicker:
    """Test suite for validating Date picker behavior."""

    def test_open_calendar(self, date_picker):
        """Verify that Calendar is displayed when date input field is clicked."""
        date_picker.tap_date_field()
        assert date_picker.is_calendar_displayed() is True, "Failed to display Calendar."

    def test_all_months(self, date_picker):
        """This test verifies that all calendar months are available and no duplicated months."""
        date_picker.tap_date_field()
        month_list=[month.text for month in date_picker.get_all_months()]
        assert month_list == CALENDAR_MONTHS,"Missing month in calendar"

    @pytest.mark.parametrize(
        "random_months",[CALENDAR_MONTHS], indirect=True)
    def test_navigate_to_random_month(self,date_picker,random_months):
        """This test navigates to random calendar months."""
        date_picker.tap_date_field()
        for month in random_months:
            date_picker.navigate_to_next_month(month)
            assert date_picker.verify_month_selected(month), f"Selected month not set: {month}."

    @pytest.mark.parametrize(
        "months",[CALENDAR_MONTHS], indirect=True)
    def test_set_random_date(self,date_picker,months):
        """This test sets a random date for each calendar month."""
        date_picker.tap_date_field()
        for month in months:
            date_picker.navigate_to_next_month(month)
            date = random.randint(1, len(date_picker.get_dates()))
            date_picker.select_date(date)
            assert date_picker.verify_date_set(date), f"Selected date not set: {date},{months}."

    def test_next_boundary_month(self, date_picker):
        """This test verifies navigation to next boundary month."""
        date_picker.tap_date_field()
        date_picker.navigate_to_next_month('Dec')
        date_picker.tap_next_icon()
        assert date_picker.verify_month_selected('Jan'), f"Selected month not set."

    def test_prev_boundary_month(self, date_picker):
        """This test verifies navigation to previous boundary month."""
        date_picker.tap_date_field()
        date_picker.navigate_to_next_month('Jan')
        date_picker.tap_prev_icon()
        assert date_picker.verify_month_selected('Dec'), f"Selected month not set."