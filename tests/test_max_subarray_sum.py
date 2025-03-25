import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_case():
    """Test a normal case with a standard input."""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == [10, 23, 3, 1]

def test_full_array():
    """Test when k is equal to array length."""
    arr = [2, 3, 4, 1, 5]
    k = 5
    assert max_subarray_sum(arr, k) == [2, 3, 4, 1, 5]

def test_k_larger_than_array():
    """Test when k is larger than array length."""
    arr = [1, 2, 3]
    k = 4
    assert max_subarray_sum(arr, k) == []

def test_zero_k():
    """Test when k is zero."""
    arr = [1, 2, 3, 4, 5]
    k = 0
    assert max_subarray_sum(arr, k) == []

def test_negative_k():
    """Test when k is negative."""
    arr = [1, 2, 3, 4, 5]
    k = -1
    assert max_subarray_sum(arr, k) == []

def test_empty_array():
    """Test with an empty array."""
    arr = []
    k = 3
    assert max_subarray_sum(arr, k) == []

def test_single_element_array():
    """Test with a single element array."""
    arr = [5]
    k = 1
    assert max_subarray_sum(arr, k) == [5]

def test_multiple_same_max_subarrays():
    """Test case where multiple subarrays could have the same max sum."""
    arr = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    k = 3
    assert max_subarray_sum(arr, k) == [3, 3, 3]