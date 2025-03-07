import pytest
import random
from src.bogosort import bogosort, is_sorted

def test_bogosort_empty_list():
    """Test sorting an empty list"""
    assert bogosort([]) == []

def test_bogosort_single_element():
    """Test sorting a list with a single element"""
    assert bogosort([5]) == [5]

def test_bogosort_already_sorted():
    """Test sorting an already sorted list"""
    sorted_list = [1, 2, 3, 4, 5]
    assert bogosort(sorted_list) == sorted_list

def test_bogosort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    reverse_sorted = [5, 4, 3, 2, 1]
    assert bogosort(reverse_sorted) == [1, 2, 3, 4, 5]

def test_bogosort_random_list():
    """Test sorting a random list of integers"""
    random.seed(42)  # For reproducibility
    unsorted_list = [5, 2, 8, 1, 9]
    result = bogosort(unsorted_list)
    assert is_sorted(result)
    assert set(result) == set(unsorted_list)

def test_bogosort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    duplicates_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = bogosort(duplicates_list)
    assert is_sorted(result)
    assert set(result) == set(duplicates_list)

def test_bogosort_with_floats():
    """Test sorting a list of floating-point numbers"""
    float_list = [3.14, 2.71, 1.41, 0.58]
    result = bogosort(float_list)
    assert is_sorted(result)
    assert set(result) == set(float_list)

def test_bogosort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        bogosort("not a list")

def test_bogosort_uncomparable_items():
    """Test that ValueError is raised for uncomparable items"""
    with pytest.raises(ValueError):
        bogosort([{}, [], None])

def test_is_sorted_function():
    """Test the is_sorted helper function"""
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([5, 4, 3, 2, 1]) == False
    assert is_sorted([]) == True
    assert is_sorted([1]) == True