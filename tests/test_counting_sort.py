import pytest
from src.counting_sort import counting_sort

def test_basic_sorting():
    """Test basic sorting of a list of non-negative integers"""
    assert counting_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_already_sorted():
    """Test sorting an already sorted list"""
    assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test sorting a reverse sorted list"""
    assert counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element"""
    assert counting_sort([42]) == [42]

def test_all_same_elements():
    """Test sorting a list with all same elements"""
    assert counting_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

def test_invalid_input_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="Counting sort only works with non-negative integers"):
        counting_sort([-1, 2, 3])

def test_invalid_input_type():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_invalid_element_type():
    """Test that non-integer elements raise a TypeError"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, "3", 4])

def test_large_range():
    """Test sorting with a large range of non-negative integers"""
    input_list = [100, 2, 56, 200, 10, 1, 500]
    assert counting_sort(input_list) == [1, 2, 10, 56, 100, 200, 500]