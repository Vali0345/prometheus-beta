import pytest
from src.longest_common_prefix import find_longest_common_prefix

def test_basic_common_prefix():
    """Test finding a basic common prefix."""
    assert find_longest_common_prefix(["flower", "flow", "flight"]) == "fl"

def test_no_common_prefix():
    """Test when no common prefix exists."""
    assert find_longest_common_prefix(["dog", "racecar", "car"]) == ""

def test_single_string():
    """Test with a single string."""
    assert find_longest_common_prefix(["hello"]) == "hello"

def test_empty_list():
    """Test with an empty list."""
    assert find_longest_common_prefix([]) == ""

def test_all_identical_strings():
    """Test with all identical strings."""
    assert find_longest_common_prefix(["abc", "abc", "abc"]) == "abc"

def test_prefix_is_entire_shortest_string():
    """Test when the prefix is the entire shortest string."""
    assert find_longest_common_prefix(["abc", "abcd", "abcde"]) == "abc"

def test_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_prefix("not a list")

def test_invalid_list_elements():
    """Test raising ValueError for non-string list elements."""
    with pytest.raises(ValueError, match="All elements must be strings"):
        find_longest_common_prefix(["valid", 123, "string"])

def test_unicode_strings():
    """Test common prefix with unicode strings."""
    assert find_longest_common_prefix(["résumé", "réserve", "réaction"]) == "ré"

def test_case_sensitive():
    """Test that prefix matching is case-sensitive."""
    assert find_longest_common_prefix(["Apple", "Appetite", "Application"]) == "A"
    assert find_longest_common_prefix(["apple", "app", "apricot"]) == "ap"