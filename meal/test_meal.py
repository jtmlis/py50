from meal import convert
import pytest


class TestConvert:

    def test_convert(self):
        assert convert("7:30") == 7.5
        assert not convert("7:29") == 7.5
        assert convert("8:30") == 8.5

    def test_convert_am(self):
        assert convert("7:30am") == 7.5
        assert convert("8:30am") == 8.5

    def test_convert_pm(self):
        assert convert("7:30pm") == 19.5
        assert convert("8:30pm") == 20.5

    def test_breakfest_time(self):
        assert convert("7:00") == "breakfest time"
        assert not convert("11:00") == "breakfast time"
