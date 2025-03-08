import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome cases."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("radar") == True

def test_non_palindromes():
    """Test non-palindrome cases."""
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("python") == False

def test_case_insensitive():
    """Test that palindrome checking is case-insensitive."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_with_punctuation_and_spaces():
    """Test palindromes with punctuation and spaces."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("race a car") == False

def test_edge_cases():
    """Test various edge cases."""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Just whitespace
    assert is_palindrome("!@#$%^") == True  # Only non-alphanumeric chars
    assert is_palindrome("12321") == True  # Numeric palindrome
    assert is_palindrome("a") == True  # Single character
    assert is_palindrome("ab") == False  # Two different characters

def test_mixed_characters():
    """Test palindromes with mixed character types."""
    assert is_palindrome("123 321") == True
    assert is_palindrome("a1b2c c2b1a") == True
    assert is_palindrome("a1b2c d2b1a") == False