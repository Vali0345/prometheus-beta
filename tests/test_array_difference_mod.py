import pytest
from src.array_difference_mod import array_difference_mod

def test_basic_array_difference_mod():
    """Test basic functionality of array_difference_mod"""
    A = [7, 5, 3, 9, 2, 8, 1, 6, 4, 0]
    B = [3, 2, 1, 4, 5, 6, 7, 8, 9, 5]
    expected = [4, 3, 2, 5, 7, 2, 4, 8, 5, 5]
    assert array_difference_mod(A, B) == expected

def test_negative_difference():
    """Test scenarios with negative differences"""
    A = [2, 3, 1, 5, 7, 0, 9, 4, 6, 8]
    B = [5, 6, 4, 8, 9, 3, 2, 7, 1, 0]
    expected = [7, 7, 7, 7, 8, 7, 7, 7, 5, 8]
    assert array_difference_mod(A, B) == expected

def test_equal_arrays():
    """Test arrays where all elements are equal"""
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert array_difference_mod(A, B) == expected

def test_invalid_input_length():
    """Test error handling for invalid input array lengths"""
    with pytest.raises(ValueError, match="Both input arrays must be of length 10"):
        array_difference_mod([1, 2, 3], [4, 5, 6])

def test_input_arrays_unchanged():
    """Verify that input arrays are not modified"""
    A = [7, 5, 3, 9, 2, 8, 1, 6, 4, 0]
    B = [3, 2, 1, 4, 5, 6, 7, 8, 9, 5]
    original_A = A.copy()
    original_B = B.copy()
    array_difference_mod(A, B)
    assert A == original_A
    assert B == original_B