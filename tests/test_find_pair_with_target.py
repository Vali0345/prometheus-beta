import pytest
from src.find_pair_with_target import find_pair_with_target

def test_find_pair_with_target_basic_case():
    """Test basic functionality of finding index pairs."""
    nums = [2, 7, 11, 15]
    target = 9
    result = find_pair_with_target(nums, target)
    assert result == [[0, 1]], "Should find the correct index pair"

def test_find_pair_with_target_multiple_pairs():
    """Test finding multiple index pairs."""
    nums = [3, 2, 4, 1, 5]
    target = 6
    result = find_pair_with_target(nums, target)
    assert sorted(result) == [[1, 2], [3, 4]], "Should find all index pairs"

def test_find_pair_with_target_no_pairs():
    """Test scenario where no pairs sum to target."""
    nums = [1, 2, 3, 4, 5]
    target = 10
    result = find_pair_with_target(nums, target)
    assert result == [], "Should return empty list when no pairs found"

def test_find_pair_with_target_duplicate_values():
    """Test handling of lists with same value at different indices."""
    nums = [3, 3, 4, 5]
    target = 6
    result = find_pair_with_target(nums, target)
    assert sorted(result) == [[0, 1]], "Should handle lists with duplicate values"

def test_find_pair_with_target_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_pair_with_target(123, 5)

def test_find_pair_with_target_invalid_target_type():
    """Test error handling for invalid target type."""
    with pytest.raises(TypeError, match="Target must be an integer"):
        find_pair_with_target([1, 2, 3], "5")

def test_find_pair_with_target_invalid_list_elements():
    """Test error handling for non-integer list elements."""
    with pytest.raises(ValueError, match="All elements in the list must be integers"):
        find_pair_with_target([1, 2, '3'], 5)

def test_find_pair_with_target_edge_case_empty_list():
    """Test behavior with an empty list."""
    nums = []
    target = 5
    result = find_pair_with_target(nums, target)
    assert result == [], "Should return empty list for empty input list"

def test_find_pair_with_target_large_numbers():
    """Test functionality with large numbers."""
    nums = [1000000, 2000000, 3000000, 4000000]
    target = 5000000
    result = find_pair_with_target(nums, target)
    assert result == [[1, 2]], "Should work with large numbers"