from Working.working import convert
import pytest


def test_colon():
    assert convert('9:50 AM to 12:30 PM') == '09:50 to 12:30'
    assert convert('8:45 PM to 11:30 AM') == '20:45 to 11:30'


def test_whole():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'


def test_value():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
        convert('8:60 AM to 4:60 PM')
        convert("9AM to 5PM")