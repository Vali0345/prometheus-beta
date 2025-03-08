import pytest
from src.max_subarray_sum import max_subarray_sum_with_constraints

def test_basic_case():
    # Basic test case where a valid subarray exists
    arr = [1, 2, 3, 4, 5]
    k = 2
    s = 8
    assert max_subarray_sum_with_constraints(arr, k, s) == 9  # 4 + 5

def test_no_valid_subarray():
    # Test case where no subarray meets the constraints
    arr = [1, 2, 3]
    k = 2
    s = 10
    assert max_subarray_sum_with_constraints(arr, k, s) == -1

def test_edge_cases():
    # Empty array
    assert max_subarray_sum_with_constraints([], 2, 5) == -1
    
    # k greater than array length
    assert max_subarray_sum_with_constraints([1, 2, 3], 4, 5) == -1
    
    # k less than or equal to 0
    assert max_subarray_sum_with_constraints([1, 2, 3], 0, 5) == -1
    assert max_subarray_sum_with_constraints([1, 2, 3], -1, 5) == -1

def test_multiple_valid_subarrays():
    # Multiple subarrays exist, should return max sum
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 3
    s = 15
    assert max_subarray_sum_with_constraints(arr, k, s) == 33  # 10, 23, 3

def test_negative_numbers():
    # Test with negative numbers
    arr = [-1, -2, 3, 4, -5, 6, 7]
    k = 3
    s = 10
    assert max_subarray_sum_with_constraints(arr, k, s) == 13  # 3, 4, 6

def test_exact_k_minimum_length():
    # Test with exactly k elements
    arr = [1, 2, 3, 4, 5]
    k = 3
    s = 10
    assert max_subarray_sum_with_constraints(arr, k, s) == 12  # 3, 4, 5

def test_large_sum_threshold():
    # Test with a large sum threshold
    arr = [1, 2, 3, 4, 5]
    k = 2
    s = 100
    assert max_subarray_sum_with_constraints(arr, k, s) == -1