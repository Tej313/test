# conftest.py
import pytest

@pytest.fixture
def number_list():
    """A simple fixture that returns a list of integers"""
    return [1, 2, 3, 4, 5]
# test_numbers.py
def test_are_integers(number_list):
    """Test to check if all elements in the list are integers"""
    for item in number_list:
        assert isinstance(item, int), f"{item} is not an integer"
