import pytest

class TestSlider:
    """Test suite for validating Slider behavior."""

    def test_slider_current_value(self, slider):
        """Verify the actual slider value."""
        default_val=5
        assert slider.get_slider_value() == default_val,"Incorrect initial slider value."

    @pytest.mark.parametrize("method, expected",[
        ("get_slider_min_value", 0),("get_slider_max_value", 10),])
    def test_slider_values(self, slider, method, expected):
        """Verify the slider max, min and default values."""
        assert getattr(slider, method)() == expected

    def test_set_slider_value(self, slider):
        """Verify the new set slider value."""
        new_val=10
        slider.set_slider_value(new_val)
        assert slider.get_slider_value() == new_val,f"Failed to set new value {new_val}."
