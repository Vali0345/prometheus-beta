import pytest
from src.median_two_sorted_arrays import find_median_sorted_arrays

def test_basic_cases():
    """Test basic scenarios with even and odd total lengths."""
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
    assert find_median_sorted_arrays([0, 0], [0, 0]) == 0.0

def test_one_empty_array():
    """Test cases where one array is empty."""
    assert find_median_sorted_arrays([], [1]) == 1.0
    assert find_median_sorted_arrays([2], []) == 2.0
    assert find_median_sorted_arrays([], [1, 2, 3, 4, 5]) == 3.0

def test_different_lengths():
    """Test arrays with significantly different lengths."""
    assert find_median_sorted_arrays([1, 3, 5], [2, 4, 6, 8, 10]) == 4.5
    assert find_median_sorted_arrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == 5.5

def test_large_numbers():
    """Test with large numbers."""
    assert find_median_sorted_arrays([100, 200], [300, 400]) == 250.0

def test_negative_numbers():
    """Test with negative numbers."""
    assert find_median_sorted_arrays([-5, -3, -1], [-2, 0, 2]) == -1.5

def test_error_cases():
    """Test error handling."""
    with pytest.raises(TypeError):
        find_median_sorted_arrays(1, [2])
    
    with pytest.raises(TypeError):
        find_median_sorted_arrays([1], "2")
    
    with pytest.raises(ValueError):
        find_median_sorted_arrays([1, 'a'], [2, 3])

def test_unsorted_input():
    """Ensure function raises error for unsorted inputs."""
    with pytest.raises(ValueError):
        find_median_sorted_arrays([3, 1], [2, 4])

def test_floating_point_inputs():
    """Test inputs with floating point numbers."""
    assert find_median_sorted_arrays([1.5, 2.5], [3.5, 4.5]) == 3.0