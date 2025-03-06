import pytest
from src.array_rotation import rotate_array

def test_basic_rotation():
    """Test basic array rotation"""
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    """Test rotation equal to array length"""
    assert rotate_array([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

def test_partial_rotation():
    """Test rotation less than array length"""
    assert rotate_array([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]

def test_empty_array():
    """Test rotation of an empty array"""
    assert rotate_array([], 3) == []

def test_single_element_array():
    """Test rotation of a single-element array"""
    assert rotate_array([1], 5) == [1]

def test_rotation_beyond_length():
    """Test rotation greater than array length"""
    assert rotate_array([1, 2, 3], 7) == [2, 3, 1]

def test_zero_rotation():
    """Test rotation of 0 positions"""
    assert rotate_array([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]

def test_invalid_input_type():
    """Test invalid input type for array"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array("not a list", 2)

def test_invalid_rotation_type():
    """Test invalid rotation type"""
    with pytest.raises(TypeError, match="Rotation positions must be an integer"):
        rotate_array([1, 2, 3], "2")

def test_negative_rotation():
    """Test negative rotation raises ValueError"""
    with pytest.raises(ValueError, match="Rotation positions must be non-negative"):
        rotate_array([1, 2, 3], -1)