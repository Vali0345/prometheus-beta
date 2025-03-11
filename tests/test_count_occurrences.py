import pytest
from src.count_occurrences import count_occurrences

def test_count_occurrences_basic():
    """Test basic occurrence counting"""
    test_list = [1, 2, 3, 2, 2, 4, 5]
    assert count_occurrences(test_list, 2) == 3

def test_count_occurrences_empty_list():
    """Test occurrence counting on an empty list"""
    assert count_occurrences([], 5) == 0

def test_count_occurrences_no_matches():
    """Test when target is not in the list"""
    test_list = [1, 2, 3, 4, 5]
    assert count_occurrences(test_list, 6) == 0

def test_count_occurrences_different_types():
    """Test with different types of elements"""
    test_list = [1, 'a', 2, 'a', 3, 'a']
    assert count_occurrences(test_list, 'a') == 3

def test_count_occurrences_invalid_input():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        count_occurrences("not a list", 1)

def test_count_occurrences_none():
    """Test counting occurrences of None"""
    test_list = [None, 1, None, 2, None]
    assert count_occurrences(test_list, None) == 3