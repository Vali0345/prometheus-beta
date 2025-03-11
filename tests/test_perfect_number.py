import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num), f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test numbers that are not perfect numbers."""
    non_perfect_numbers = [1, 2, 3, 4, 5, 10, 100]
    for num in non_perfect_numbers:
        assert not is_perfect_number(num), f"{num} should not be a perfect number"

def test_zero_and_negative():
    """Test that zero and negative numbers are not perfect numbers."""
    assert not is_perfect_number(0), "0 should not be a perfect number"
    assert not is_perfect_number(-6), "Negative numbers should not be perfect numbers"

def test_invalid_input_types():
    """Test that invalid input types raise a ValueError."""
    with pytest.raises(ValueError):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError):
        is_perfect_number("6")
    
    with pytest.raises(ValueError):
        is_perfect_number(None)