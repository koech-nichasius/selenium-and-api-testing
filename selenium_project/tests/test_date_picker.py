class TestDatePicker:
    """Test suite for validating Date picker behavior."""

    def test_open_calendar(self, date_picker):
        """Verify that Calendar is displayed when date input field is clicked."""
        date_picker.tap_date_field()
        assert date_picker.is_calendar_displayed() is True, "Failed to display Calendar."

    def test_every_month(self, date_picker):
        """This test checks that all calendar months are available."""
        date_picker.tap_date_field()
        expected_list=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month_list=[month.text for month in date_picker.get_all_months()]
        assert month_list == expected_list,"Missing month in calendar"

    def test_set_date(self,date_picker, month):
        """This test sets each date for every calendar month."""
        date_picker.tap_date_field()
        date_picker.select_month(month)
        dates=len(date_picker.get_dates())+1
        for date in range(1, dates):
            date_picker.select_date(date)
            assert date_picker.verify_date_set(date), f"Selected date not set: {date},{month}."



