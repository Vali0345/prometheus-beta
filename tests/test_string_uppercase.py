import pytest
from src.string_uppercase import convert_to_uppercase_with_spaces

def test_convert_to_uppercase_with_spaces():
    # Test basic conversion
    assert convert_to_uppercase_with_spaces("hello world") == "HELLO WORLD"
    
    # Test string with multiple spaces
    assert convert_to_uppercase_with_spaces("hello   world") == "HELLO WORLD"
    
    # Test string with leading/trailing spaces
    assert convert_to_uppercase_with_spaces("  hello world  ") == "HELLO WORLD"
    
    # Test single word
    assert convert_to_uppercase_with_spaces("hello") == "HELLO"
    
    # Test empty string
    assert convert_to_uppercase_with_spaces("") == ""
    
    # Test string with mixed case
    assert convert_to_uppercase_with_spaces("HeLLo WoRLd") == "HELLO WORLD"

def test_convert_to_uppercase_with_spaces_error_handling():
    # Test non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase_with_spaces(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase_with_spaces(["hello"])