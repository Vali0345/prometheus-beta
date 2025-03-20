import pytest
from src.max_subarray_sum import max_subarray_sum

def test_standard_case():
    """Test with a standard array and valid k"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1

def test_all_positive_numbers():
    """Test with an array of all positive numbers"""
    arr = [5, 6, 7, 8, 9]
    k = 3
    assert max_subarray_sum(arr, k) == 24  # 7 + 8 + 9

def test_all_negative_numbers():
    """Test with an array of all negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    k = 2
    assert max_subarray_sum(arr, k) == -3  # -1 + -2

def test_mixed_numbers():
    """Test with an array of mixed positive and negative numbers"""
    arr = [1, -3, 4, -2, 5, -1, 3]
    k = 3
    assert max_subarray_sum(arr, k) == 7  # 4 + -2 + 5

def test_k_equals_array_length():
    """Test when k is equal to the array length"""
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert max_subarray_sum(arr, k) == 15

def test_empty_array():
    """Test with an empty array"""
    arr = []
    k = 3
    assert max_subarray_sum(arr, k) is None

def test_k_greater_than_array_length():
    """Test when k is larger than array length"""
    arr = [1, 2, 3]
    k = 4
    assert max_subarray_sum(arr, k) is None

def test_invalid_k_raises_error():
    """Test that invalid k raises a ValueError"""
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError):
        max_subarray_sum(arr, 0)
    
    with pytest.raises(ValueError):
        max_subarray_sum(arr, -1)