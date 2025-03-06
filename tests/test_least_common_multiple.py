import pytest
from src.least_common_multiple import find_lcm

def test_lcm_basic_positive_numbers():
    """Test LCM of basic positive numbers"""
    assert find_lcm(4, 6) == 12
    assert find_lcm(21, 6) == 42
    assert find_lcm(17, 5) == 85

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers"""
    assert find_lcm(7, 13) == 91
    assert find_lcm(11, 17) == 187

def test_lcm_one_number_multiple_of_other():
    """Test LCM when one number is a multiple of the other"""
    assert find_lcm(8, 4) == 8
    assert find_lcm(15, 5) == 15

def test_lcm_same_numbers():
    """Test LCM of the same number"""
    assert find_lcm(7, 7) == 7

def test_lcm_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_lcm(4.5, 6)
    
    with pytest.raises(TypeError):
        find_lcm("4", 6)
    
    with pytest.raises(ValueError):
        find_lcm(0, 6)
    
    with pytest.raises(ValueError):
        find_lcm(4, -6)
    
    with pytest.raises(ValueError):
        find_lcm(-4, -6)