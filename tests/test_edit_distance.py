import pytest
from src.edit_distance import edit_distance

def test_edit_distance_same_strings():
    """Test edit distance for identical strings"""
    assert edit_distance("hello", "hello") == 0

def test_edit_distance_empty_strings():
    """Test edit distance with empty strings"""
    assert edit_distance("", "") == 0
    assert edit_distance("hello", "") == 5
    assert edit_distance("", "world") == 5

def test_edit_distance_different_lengths():
    """Test edit distance for strings of different lengths"""
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("saturday", "sunday") == 3

def test_edit_distance_case_sensitive():
    """Test edit distance is case-sensitive"""
    assert edit_distance("Hello", "hello") == 1

def test_edit_distance_complex_cases():
    """Test more complex edit distance scenarios"""
    assert edit_distance("intention", "execution") == 5
    assert edit_distance("book", "back") == 2

def test_edit_distance_unicode():
    """Test edit distance with unicode strings"""
    assert edit_distance("café", "cafe") == 1
    assert edit_distance("résumé", "resume") == 2

def test_edit_distance_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        edit_distance(123, "hello")
    with pytest.raises(TypeError):
        edit_distance("hello", None)
    with pytest.raises(TypeError):
        edit_distance(None, None)