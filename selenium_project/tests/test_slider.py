import random
import pytest
from selenium_project.config import DEFAULT_SLIDER_VAL, MIN_SLIDER_VAL, MAX_SLIDER_VAL


class TestSlider:
    """Test suite for validating Slider behavior."""

    def test_slider_current_value(self, slider):
        """Verify the actual slider value."""
        assert slider.get_slider_value() == DEFAULT_SLIDER_VAL, "Incorrect initial slider value."

    @pytest.mark.parametrize("method, expected", [
        ("get_slider_min_value", MIN_SLIDER_VAL),("get_slider_max_value", MAX_SLIDER_VAL),])
    def test_slider_values(self, slider, method, expected):
        """Verify the slider max, min and default values."""
        assert getattr(slider, method)() == expected

    def test_set_slider_value(self, slider):
        """Verify the new set slider value."""
        slider.set_slider_value(MAX_SLIDER_VAL)
        assert slider.get_slider_value() == MAX_SLIDER_VAL, f"Failed to set new value {MAX_SLIDER_VAL}."

    def test_set_exceed_max(self, slider):
        """Verify the new set slider value exceeding max value."""
        new_val = random.randint(100, 200)
        slider.set_slider_value(new_val)
        assert slider.get_slider_value() == MAX_SLIDER_VAL, f"Failed to set new value {MAX_SLIDER_VAL}."

    def test_set_negative_value(self, slider):
        """Verify the new set slider value less than min value."""
        new_val = random.randint(-100, 0)
        slider.set_slider_value(new_val)
        assert slider.get_slider_value() == MIN_SLIDER_VAL, f"Failed to set new value {MIN_SLIDER_VAL}."