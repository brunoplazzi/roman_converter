from src.roman_converter import int_to_roman
import pytest


def test_single_digit():
    assert int_to_roman(1) == "I"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(9) == "IX"


def test_double_digit():
    assert int_to_roman(10) == "X"
    assert int_to_roman(40) == "XL"
    assert int_to_roman(99) == "XCIX"


def test_triple_digit():
    assert int_to_roman(100) == "C"
    assert int_to_roman(400) == "CD"
    assert int_to_roman(999) == "CMXCIX"


def test_large_numbers():
    assert int_to_roman(1000) == "M"
    assert int_to_roman(3999) == "MMMCMXCIX"


def test_invalid_input():
    with pytest.raises(ValueError):
        int_to_roman(0)
    with pytest.raises(ValueError):
        int_to_roman(4000)
