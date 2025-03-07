import pytest
from src.nested_list_flatten import flatten_nested_list

def test_basic_flatten():
    """Test basic list flattening"""
    assert flatten_nested_list([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_empty_list():
    """Test flattening an empty list"""
    assert flatten_nested_list([]) == []

def test_no_nesting():
    """Test list with no nesting"""
    assert flatten_nested_list([1, 2, 3]) == [1, 2, 3]

def test_deeply_nested_list():
    """Test deeply nested list"""
    assert flatten_nested_list([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_mixed_iterables():
    """Test list with mixed iterables"""
    assert flatten_nested_list([1, (2, 3), [4, {5, 6}]]) == [1, 2, 3, 4, 5, 6]

def test_error_non_iterable():
    """Test error handling for non-iterable input"""
    with pytest.raises(TypeError):
        flatten_nested_list(42)

def test_error_string():
    """Test that strings are not recursively flattened"""
    assert flatten_nested_list(["hello", ["world"]]) == ["hello", "world"]