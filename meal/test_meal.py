from meal import convert, meal_time
import pytest


class TestConvert:

    def test_convert(self):
        assert convert("7:30") == 7.5
        assert not convert("7:29") == 7.5
        assert convert("8:30") == 8.5

    def test_convert_am(self):
        assert convert("7:30am") == 7.5
        assert convert("8:30am") == 8.5
# Not ready yet
 #   def test_convert_pm(self):
 #       assert convert("7:30pm") == 19.5
 #      assert convert("8:30pm") == 20.5

    def test_meal_time(self):
        assert meal_time(7.5) == "breakfast time"
        assert meal_time(11) == "breakfast time"
