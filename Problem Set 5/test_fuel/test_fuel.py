# Problem statement: https://cs50.harvard.edu/python/2022/psets/5/test_fuel/
import pytest
from fuel import convert,gauge

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("3/1")

def test_convert():
    assert convert("1/2") == 50
    assert convert("99/100") == 99
    assert convert("1/100") == 1


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
