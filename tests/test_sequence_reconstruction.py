import pytest
from src.sequence_reconstruction import min_reconstruction_operations

def test_identical_sequences():
    """Test when sequences are identical"""
    assert min_reconstruction_operations([1, 2, 3], [1, 2, 3]) == 0

def test_different_length_sequences():
    """Test sequences of different lengths"""
    assert min_reconstruction_operations([1, 2, 3], [1, 2]) == 1
    assert min_reconstruction_operations([1, 2], [1, 2, 3]) == 1

def test_completely_different_sequences():
    """Test completely different sequences"""
    assert min_reconstruction_operations([1, 2, 3], [4, 5, 6]) == 6

def test_repeated_elements():
    """Test sequences with repeated elements"""
    assert min_reconstruction_operations([1, 1, 2, 2], [1, 2]) == 2
    assert min_reconstruction_operations([1, 2], [1, 1, 2, 2]) == 2

def test_empty_sequences():
    """Test empty sequences"""
    assert min_reconstruction_operations([], []) == 0
    assert min_reconstruction_operations([], [1, 2]) == 2
    assert min_reconstruction_operations([1, 2], []) == 2

def test_invalid_input():
    """Test invalid input types"""
    with pytest.raises(ValueError):
        min_reconstruction_operations("not a list", [1, 2])
    with pytest.raises(ValueError):
        min_reconstruction_operations([1, 2], "not a list")

def test_mixed_type_elements():
    """Test sequences with mixed type elements"""
    assert min_reconstruction_operations([1, 'a', 2], ['a', 3]) == 3