import pytest
from src.multiply_array import multiply

def test_multiply_basic():
    """Test basic multiplication of array elements."""
    assert multiply([1, 2, 3]) == [1, 2, 3]

def test_multiply_empty_list():
    """Test behavior with an empty list."""
    assert multiply([]) == []

def test_multiply_single_element():
    """Test behavior with a single-element list."""
    assert multiply([5]) == [5]

def test_multiply_negative_numbers():
    """Test multiplication with negative numbers."""
    assert multiply([-1, -2, -3]) == [-1, -2, -3]

def test_multiply_float_numbers():
    """Test multiplication with float numbers."""
    assert multiply([1.5, 2.0, 3.5]) == [1.5, 2.0, 3.5]

def test_invalid_input_type():
    """Test raising ValueError for non-list input."""
    with pytest.raises(ValueError, match="Input must be a list"):
        multiply("not a list")

def test_invalid_element_type():
    """Test raising ValueError for non-numeric elements."""
    with pytest.raises(ValueError, match="All elements must be numeric"):
        multiply([1, 2, "three"])