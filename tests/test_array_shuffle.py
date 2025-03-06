import pytest
import random
from src.array_shuffle import shuffle_array

def test_shuffle_basic_list():
    """Test shuffling a basic list of integers"""
    original = [1, 2, 3, 4, 5]
    # We can't assert exact randomness, but we can check:
    # 1. The result is a list
    # 2. The result has the same length
    # 3. The result contains the same elements
    shuffled = shuffle_array(original)
    
    assert isinstance(shuffled, list)
    assert len(shuffled) == len(original)
    assert sorted(shuffled) == sorted(original)

def test_shuffle_empty_list():
    """Test shuffling an empty list"""
    assert shuffle_array([]) == []

def test_shuffle_single_element_list():
    """Test shuffling a list with a single element"""
    single_element = [42]
    assert shuffle_array(single_element) == single_element

def test_shuffle_string_list():
    """Test shuffling a list of strings"""
    original = ["apple", "banana", "cherry", "date"]
    shuffled = shuffle_array(original)
    
    assert isinstance(shuffled, list)
    assert len(shuffled) == len(original)
    assert sorted(shuffled) == sorted(original)

def test_shuffle_is_random():
    """Probabilistic test to ensure some randomness"""
    # This is a statistical test to check for basic randomness
    original = list(range(10))
    shuffles = [shuffle_array(original) for _ in range(100)]
    
    # Ensure that at least some shuffles are different from the original
    # and from each other (very high probability)
    different_shuffles = set(tuple(shuffle) for shuffle in shuffles)
    assert len(different_shuffles) > 1

def test_shuffle_does_not_modify_original():
    """Ensure the original list is not modified"""
    original = [1, 2, 3, 4, 5]
    _ = shuffle_array(original)
    assert original == [1, 2, 3, 4, 5]

def test_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError):
        shuffle_array(123)
    
    with pytest.raises(TypeError):
        shuffle_array(None)