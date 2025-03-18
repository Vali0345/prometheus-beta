import pytest
from src.longest_substring import find_longest_substring

def test_find_longest_substring_basic():
    """Test basic functionality of finding longest substring."""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_find_longest_substring_edge_cases():
    """Test edge cases for the function."""
    assert find_longest_substring("") == ""
    assert find_longest_substring("a") == "a"
    assert find_longest_substring("ab") == "ab"

def test_find_longest_substring_case_sensitive():
    """Ensure the function is case-sensitive."""
    assert find_longest_substring("aA") == "aA"
    assert find_longest_substring("AbcA") == "Abc"

def test_find_longest_substring_special_chars():
    """Test with special characters and mixed input."""
    assert find_longest_substring("!@#$%") == "!@#$%"
    assert find_longest_substring("hello") in ["hel", "ello"]

def test_find_longest_substring_repeated_sections():
    """Test scenarios with multiple repeated sections."""
    assert find_longest_substring("dvdf") == "vdf"
    assert find_longest_substring("tmmzuxt") == "mzuxt"