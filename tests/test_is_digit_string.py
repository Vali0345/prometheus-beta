import pytest
from src.is_digit_string import is_digit_string

def test_valid_digit_string():
    """Test strings containing only digits."""
    assert is_digit_string("12345") == True
    assert is_digit_string("0") == True
    assert is_digit_string("9876543210") == True

def test_invalid_digit_string():
    """Test strings that are not purely digits."""
    assert is_digit_string("123.45") == False
    assert is_digit_string("12a34") == False
    assert is_digit_string("") == False
    assert is_digit_string(" ") == False
    assert is_digit_string("abc") == False

def test_error_cases():
    """Test error handling."""
    with pytest.raises(TypeError):
        is_digit_string(12345)
    
    with pytest.raises(TypeError):
        is_digit_string(None)

def test_edge_cases():
    """Test various edge cases."""
    # Negative sign is not considered a digit
    assert is_digit_string("-123") == False
    
    # Whitespace is not considered a digit
    assert is_digit_string("  123  ") == False
    
    # Unicode characters that look like digits are not considered
    assert is_digit_string("１２３") == False  # Full-width digits