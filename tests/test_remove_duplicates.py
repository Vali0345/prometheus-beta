import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicates_basic():
    """Test basic string deduplication."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbccdd") == "abcd"

def test_remove_duplicates_empty_string():
    """Test handling of empty string."""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicates_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicate_chars("abcdef") == "abcdef"

def test_remove_duplicates_preserve_order():
    """Test that original order is preserved."""
    assert remove_duplicate_chars("cabbage") == "cabge"

def test_remove_duplicates_mixed_chars():
    """Test string with mixed case and special characters."""
    assert remove_duplicate_chars("AaBbCcAaBb") == "AaBbCc"

def test_remove_duplicates_invalid_input():
    """Test handling of non-string inputs."""
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)

def test_remove_duplicates_spaces_and_symbols():
    """Test handling of whitespace and symbols."""
    assert remove_duplicate_chars("  hello  world  ") == " hello world"
    assert remove_duplicate_chars("a!b!c!a") == "a!b!c"