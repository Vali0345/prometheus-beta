import pytest
from src.alternating_snake_case import to_alternating_snake_case

def test_basic_conversion():
    """Test basic string conversion to alternating snake case."""
    assert to_alternating_snake_case("hello world") == "hello_WORLD"
    assert to_alternating_snake_case("python programming language") == "python_PROGRAMMING_language"

def test_single_word():
    """Test conversion with a single word."""
    assert to_alternating_snake_case("hello") == "hello"
    assert to_alternating_snake_case("WORLD") == "world"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_snake_case("") == ""

def test_multiple_words():
    """Test conversion with multiple words."""
    assert to_alternating_snake_case("one two three four") == "one_TWO_three_FOUR"

def test_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_snake_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_snake_case(None)

def test_whitespace_handling():
    """Test handling of multiple whitespaces."""
    assert to_alternating_snake_case("  hello   world  ") == "hello_WORLD"

def test_mixed_case_input():
    """Test input with mixed case."""
    assert to_alternating_snake_case("HeLLo WoRLD") == "hello_WORLD"