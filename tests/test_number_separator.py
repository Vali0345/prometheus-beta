import pytest
from src.number_separator import separate_evens_odds

def test_separate_evens_odds_mixed_numbers():
    """Test separating a list with mixed even and odd numbers."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens, odds = separate_evens_odds(input_list)
    assert evens == [2, 4, 6, 8, 10]
    assert odds == [1, 3, 5, 7, 9]

def test_separate_evens_odds_only_evens():
    """Test a list containing only even numbers."""
    input_list = [2, 4, 6, 8, 10]
    evens, odds = separate_evens_odds(input_list)
    assert evens == [2, 4, 6, 8, 10]
    assert odds == []

def test_separate_evens_odds_only_odds():
    """Test a list containing only odd numbers."""
    input_list = [1, 3, 5, 7, 9]
    evens, odds = separate_evens_odds(input_list)
    assert evens == []
    assert odds == [1, 3, 5, 7, 9]

def test_separate_evens_odds_empty_list():
    """Test an empty input list."""
    input_list = []
    evens, odds = separate_evens_odds(input_list)
    assert evens == []
    assert odds == []

def test_separate_evens_odds_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        separate_evens_odds(42)

def test_separate_evens_odds_invalid_element_type():
    """Test that a TypeError is raised when list contains non-integers."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        separate_evens_odds([1, 2, 'three', 4])

def test_separate_evens_odds_zero_handling():
    """Test handling of zero, which is considered an even number."""
    input_list = [-1, 0, 1, 2, -2]
    evens, odds = separate_evens_odds(input_list)
    assert evens == [0, 2, -2]
    assert odds == [-1, 1]