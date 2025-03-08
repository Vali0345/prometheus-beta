import pytest
from src.local_maxima import find_local_maxima


def test_find_local_maxima_typical_case():
    """Test finding local maxima in a typical array."""
    assert find_local_maxima([1, 3, 2, 4, 1, 5]) == [3, 4, 5]


def test_find_local_maxima_single_element():
    """Test that a single element is returned as a local maximum."""
    assert find_local_maxima([42]) == [42]


def test_find_local_maxima_sorted_ascending():
    """Test an array with ascending values."""
    assert find_local_maxima([1, 2, 3, 4, 5]) == [5]


def test_find_local_maxima_sorted_descending():
    """Test an array with descending values."""
    assert find_local_maxima([5, 4, 3, 2, 1]) == [5]


def test_find_local_maxima_equal_elements():
    """Test an array with equal elements."""
    assert find_local_maxima([1, 1, 1, 1]) == []


def test_find_local_maxima_multiple_peaks():
    """Test an array with multiple local maxima."""
    assert find_local_maxima([1, 3, 1, 4, 2, 5, 1]) == [3, 4, 5]


def test_find_local_maxima_invalid_input_empty():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_local_maxima([])


def test_find_local_maxima_invalid_input_type():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_local_maxima("not a list")
        find_local_maxima(123)
        find_local_maxima(None)