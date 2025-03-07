import pytest
from src.palindrome_validator import is_palindrome

def test_classic_palindromes():
    """Test well-known palindromes with punctuation and spaces."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_simple_palindromes():
    """Test simple palindromes with different cases."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaceCar") == True

def test_edge_cases():
    """Test edge cases like empty string and single character."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("!!!") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_mixed_case_palindromes():
    """Test palindromes with mixed case and punctuation."""
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No 'x' in Nixon") == True

def test_numeric_palindromes():
    """Test numeric palindromes."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("1 2 3 2 1") == True
    
def test_non_alphanumeric_strings():
    """Test strings with only non-alphanumeric characters."""
    assert is_palindrome("!@#$%^&*()") == True
    assert is_palindrome("") == True