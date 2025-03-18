import pytest
import random
from src.tim_sort import tim_sort

def test_tim_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert tim_sort(arr) == []

def test_tim_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert tim_sort(arr) == [42]

def test_tim_sort_sorted_list():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert tim_sort(arr) == [1, 2, 3, 4, 5]

def test_tim_sort_reverse_sorted_list():
    """Test sorting a reverse sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert tim_sort(arr) == [1, 2, 3, 4, 5]

def test_tim_sort_random_list():
    """Test sorting a random list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert tim_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_tim_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert tim_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_tim_sort_large_random_list():
    """Test sorting a large random list."""
    arr = [random.randint(-1000, 1000) for _ in range(1000)]
    sorted_arr = tim_sort(arr.copy())
    assert sorted_arr == sorted(arr)

def test_tim_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-5, -2, -8, -1, -9]
    assert tim_sort(arr) == [-9, -8, -5, -2, -1]

def test_tim_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers."""
    arr = [-5, 2, 0, -8, 7, 1]
    assert tim_sort(arr) == [-8, -5, 0, 1, 2, 7]

def test_tim_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        tim_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        tim_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        tim_sort(None)