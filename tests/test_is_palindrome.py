import pytest
from src.is_palindrome import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_non_palindromes():
    """Test non-palindrome scenarios"""
    assert is_palindrome("hello") == False
    assert is_palindrome("race a car") == False

def test_edge_cases():
    """Test edge cases"""
    assert is_palindrome("") == True  # Empty string is a palindrome
    assert is_palindrome(" ") == True  # Whitespace-only string
    assert is_palindrome("!@#$%^&*()") == True  # Special characters only

def test_case_sensitivity():
    """Test case-insensitive palindrome checking"""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("A") == True
    
def test_punctuation_and_spaces():
    """Test palindromes with punctuation and spaces"""
    assert is_palindrome("No 'x' in Nixon") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_numbers():
    """Test palindromes with numbers"""
    assert is_palindrome("123321") == True
    assert is_palindrome("12 321") == True
    assert is_palindrome("12345") == False