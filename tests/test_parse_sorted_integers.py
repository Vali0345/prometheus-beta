import pytest
from src.parse_sorted_integers import parse_sorted_comma_integers

def test_basic_integer_parsing():
    """Test basic comma-separated integer parsing."""
    assert parse_sorted_comma_integers("1,2,3") == [1, 2, 3]

def test_mixed_string_input():
    """Test parsing with non-integer characters."""
    assert parse_sorted_comma_integers("10,2abc,3def") == [2, 3, 10]

def test_empty_string():
    """Test parsing an empty string."""
    assert parse_sorted_comma_integers("") == []

def test_single_integer():
    """Test parsing a single integer."""
    assert parse_sorted_comma_integers("42") == [42]

def test_repeated_integers():
    """Test parsing repeated integers."""
    assert parse_sorted_comma_integers("5,5,3,3,1") == [1, 3, 3, 5, 5]

def test_large_integers():
    """Test parsing large integers."""
    assert parse_sorted_comma_integers("1000000,500,999999") == [500, 1000000, 999999]

def test_whitespace_and_mixed_input():
    """Test parsing with whitespace and mixed inputs."""
    assert parse_sorted_comma_integers(" 10 , 2abc , 3def ") == [2, 3, 10]

def test_no_valid_integers():
    """Test input with no valid integers."""
    assert parse_sorted_comma_integers("abc,def,ghi") == []