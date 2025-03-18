import pytest
from src.middle_range_indices import find_middle_range_indices

def test_odd_length_list_default_range():
    """Test function with odd-length list and default range"""
    test_list = [1, 2, 3, 4, 5, 6, 7]
    assert find_middle_range_indices(test_list, 1) == [2, 3, 4]

def test_even_length_list_default_range():
    """Test function with even-length list and default range"""
    test_list = [1, 2, 3, 4, 5, 6]
    assert find_middle_range_indices(test_list, 1) == [2, 3]

def test_large_range_limited_by_list_start():
    """Test when range would extend before list start"""
    test_list = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(test_list, 3) == [0, 1, 2, 3, 4]

def test_large_range_limited_by_list_end():
    """Test when range would extend past list end"""
    test_list = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(test_list, 3) == [0, 1, 2, 3, 4]

def test_zero_range():
    """Test with zero range radius"""
    test_list = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(test_list, 0) == [2]

def test_empty_list_raises_error():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_middle_range_indices([], 1)

def test_negative_range_raises_error():
    """Test that negative range radius raises ValueError"""
    with pytest.raises(ValueError, match="Range radius must be non-negative"):
        find_middle_range_indices([1, 2, 3], -1)

def test_non_list_input_raises_error():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_middle_range_indices("not a list", 1)

def test_non_integer_range_raises_error():
    """Test that non-integer range radius raises TypeError"""
    with pytest.raises(TypeError, match="Range radius must be an integer"):
        find_middle_range_indices([1, 2, 3], "1")