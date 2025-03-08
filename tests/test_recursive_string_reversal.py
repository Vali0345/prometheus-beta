import pytest
from src.recursive_string_reversal import recursive_reverse_string

def test_recursive_reverse_string_basic():
    """Test basic string reversal"""
    assert recursive_reverse_string("hello") == "olleh"
    assert recursive_reverse_string("python") == "nohtyp"

def test_recursive_reverse_string_empty():
    """Test empty string"""
    assert recursive_reverse_string("") == ""

def test_recursive_reverse_string_single_char():
    """Test single character string"""
    assert recursive_reverse_string("a") == "a"

def test_recursive_reverse_string_palindrome():
    """Test palindrome strings"""
    assert recursive_reverse_string("racecar") == "racecar"
    assert recursive_reverse_string("level") == "level"

def test_recursive_reverse_string_with_spaces():
    """Test string with spaces"""
    assert recursive_reverse_string("hello world") == "dlrow olleh"

def test_recursive_reverse_string_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse_string(None)

def test_recursive_reverse_string_special_chars():
    """Test string with special characters"""
    assert recursive_reverse_string("a1b2c3") == "3c2b1a"
    assert recursive_reverse_string("!@#$%^") == "^%$#@!"