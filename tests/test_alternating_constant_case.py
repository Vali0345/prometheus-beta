import pytest
from src.alternating_constant_case import to_alternating_constant_case

def test_basic_string():
    """Test conversion of a basic string to constant case."""
    assert to_alternating_constant_case("hello") == "HELLO"

def test_multiple_words():
    """Test conversion of a multi-word string to constant case."""
    assert to_alternating_constant_case("hello world") == "HELLO WORLD"

def test_mixed_case():
    """Test conversion of a mixed case string to constant case."""
    assert to_alternating_constant_case("Python Is Awesome") == "PYTHON IS AWESOME"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_constant_case("") == ""

def test_string_with_numbers():
    """Test conversion of a string with numbers."""
    assert to_alternating_constant_case("hello123 world") == "HELLO123 WORLD"

def test_string_with_special_characters():
    """Test conversion of a string with special characters."""
    assert to_alternating_constant_case("hello, world!") == "HELLO, WORLD!"

def test_non_string_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_constant_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_constant_case(None)