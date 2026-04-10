import pytest

class TestDropdown:
    """Test suite for validating Dropdown behavior."""

    def test_default_option(self, dropdown_page):
        """Verify the dropdown displays the expected default option."""
        assert dropdown_page.is_option_selected(
            "Open this select menu"), "Default option should be 'Open this select menu'."

    @pytest.mark.parametrize("param", ["One", "Two", "Three"])
    def test_valid_options(self, dropdown_page, param):
        """Verify that each option in the dropdown can be selected."""
        dropdown_page.select_option(param)
        assert dropdown_page.is_option_selected(param), f"Expected option '{param}' to be selected."