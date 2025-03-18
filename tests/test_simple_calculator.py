import pytest
from src.simple_calculator import simple_calculator

def test_addition():
    """Test addition operation"""
    assert simple_calculator(5, 3, '+') == 8
    assert simple_calculator(-1, 1, '+') == 0
    assert simple_calculator(2.5, 1.5, '+') == 4.0

def test_subtraction():
    """Test subtraction operation"""
    assert simple_calculator(10, 4, '-') == 6
    assert simple_calculator(-5, 3, '-') == -8
    assert simple_calculator(5.5, 2.5, '-') == 3.0

def test_multiplication():
    """Test multiplication operation"""
    assert simple_calculator(5, 3, '*') == 15
    assert simple_calculator(-2, 4, '*') == -8
    assert simple_calculator(2.5, 2, '*') == 5.0

def test_division():
    """Test division operation"""
    assert simple_calculator(10, 2, '/') == 5
    assert simple_calculator(-6, 3, '/') == -2
    assert simple_calculator(5.0, 2, '/') == 2.5

def test_division_by_zero():
    """Test division by zero raises ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        simple_calculator(10, 0, '/')

def test_invalid_operator():
    """Test invalid operator raises ValueError"""
    with pytest.raises(ValueError, match="Unsupported operator"):
        simple_calculator(5, 3, '%')

def test_type_conversion():
    """Test type conversion handling"""
    assert simple_calculator('5', '3', '+') == 8
    assert simple_calculator('10', 2, '/') == 5.0