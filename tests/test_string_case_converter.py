import pytest
from src.string_case_converter import convert_to_lowercase_with_spaces

def test_convert_to_lowercase_with_spaces():
    """Test basic string conversion to lowercase."""
    assert convert_to_lowercase_with_spaces("HELLO WORLD") == "hello world"
    assert convert_to_lowercase_with_spaces("Python Programming") == "python programming"

def test_convert_to_lowercase_with_spaces_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_lowercase_with_spaces("") == ""

def test_convert_to_lowercase_with_spaces_already_lowercase():
    """Test conversion of a string already in lowercase."""
    assert convert_to_lowercase_with_spaces("hello world") == "hello world"

def test_convert_to_lowercase_with_spaces_mixed_case():
    """Test conversion of a mixed-case string."""
    assert convert_to_lowercase_with_spaces("HeLLo WoRLD") == "hello world"

def test_convert_to_lowercase_with_spaces_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(["list"])