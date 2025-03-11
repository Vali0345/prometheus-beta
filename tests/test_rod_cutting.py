import pytest
from src.rod_cutting import rod_cutting

def test_rod_cutting_basic_case():
    """Test basic rod cutting scenario"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 10  # Original test case

def test_rod_cutting_zero_length():
    """Test rod with zero length"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 0) == 0

def test_rod_cutting_empty_prices():
    """Test with empty prices list"""
    assert rod_cutting([], 5) == 0

def test_rod_cutting_small_examples():
    """Test various small example scenarios"""
    # Test single rod length 1
    assert rod_cutting([1], 1) == 1
    
    # Test with short price list
    assert rod_cutting([1, 5], 2) == 5
    
    # Test longer scenario
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 8) == 22  # Realistic optimal value

def test_rod_cutting_uneven_lengths():
    """Test when rod length is longer than price list"""
    prices = [1, 5, 8]
    assert rod_cutting(prices, 5) == 11  # Original test case

def test_rod_cutting_complex_scenario():
    """More complex rod cutting scenario"""
    prices = [3, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 10  # Original test case