import pytest
from src.rotated_array_search import search_rotated_sorted_array

def test_search_rotated_sorted_array_basic():
    """Test basic functionality of searching in a rotated sorted array"""
    arr = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated_sorted_array(arr, 0) == 4
    assert search_rotated_sorted_array(arr, 3) == -1

def test_search_rotated_sorted_array_edge_cases():
    """Test edge cases like single element, empty array, etc."""
    # Single element array
    assert search_rotated_sorted_array([1], 1) == 0
    assert search_rotated_sorted_array([1], 0) == -1
    
    # Empty array
    assert search_rotated_sorted_array([], 5) == -1

def test_search_rotated_sorted_array_no_rotation():
    """Test when array is not rotated (fully sorted)"""
    arr = [1, 2, 3, 4, 5, 6, 7]
    assert search_rotated_sorted_array(arr, 4) == 3
    assert search_rotated_sorted_array(arr, 8) == -1

def test_search_rotated_sorted_array_all_locations():
    """Test finding elements at various locations"""
    arr = [4, 5, 6, 7, 0, 1, 2]
    # First element
    assert search_rotated_sorted_array(arr, 4) == 0
    # Last element
    assert search_rotated_sorted_array(arr, 2) == 6
    # Middle elements in both sorted halves
    assert search_rotated_sorted_array(arr, 5) == 1
    assert search_rotated_sorted_array(arr, 1) == 5

def test_search_rotated_sorted_array_error_handling():
    """Test error handling for invalid inputs"""
    # Non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        search_rotated_sorted_array("not a list", 5)
    
    # Non-integer target
    with pytest.raises(TypeError, match="Target must be an integer"):
        search_rotated_sorted_array([1, 2, 3], "5")

def test_search_rotated_sorted_array_large_input():
    """Test with a larger rotated sorted array"""
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    assert search_rotated_sorted_array(arr, 5) == 8
    assert search_rotated_sorted_array(arr, 15) == 0