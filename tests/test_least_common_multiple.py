import pytest
from src.least_common_multiple import find_lcm

def test_lcm_basic_numbers():
    """Test LCM of basic positive integers"""
    assert find_lcm(4, 6) == 12
    assert find_lcm(21, 6) == 42
    assert find_lcm(17, 5) == 85

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert find_lcm(7, 7) == 7

def test_lcm_one_is_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert find_lcm(8, 16) == 16
    assert find_lcm(16, 8) == 16

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers"""
    assert find_lcm(5, 7) == 35
    assert find_lcm(11, 13) == 143

def test_lcm_zero_input():
    """Test that zero or negative inputs raise ValueError"""
    with pytest.raises(ValueError):
        find_lcm(0, 5)
    
    with pytest.raises(ValueError):
        find_lcm(5, 0)
    
    with pytest.raises(ValueError):
        find_lcm(-3, 5)
    
    with pytest.raises(ValueError):
        find_lcm(5, -3)

def test_lcm_large_numbers():
    """Test LCM with larger numbers"""
    assert find_lcm(1000, 1500) == 3000