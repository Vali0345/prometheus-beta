import pytest
from src.kmp_string_matching import kmp_search, compute_lps

def test_compute_lps():
    """Test the computation of the Longest Proper Prefix Suffix (LPS) array."""
    assert compute_lps("AAAA") == [0, 1, 2, 3]
    assert compute_lps("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps("AABAACAABAA") == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    assert compute_lps("") == []

def test_kmp_search_basic():
    """Test basic string matching scenarios."""
    # Single occurrence
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [9]
    
    # Multiple occurrences
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    
    # No occurrences
    assert kmp_search("ABCDABCD", "XYZ") == []

def test_kmp_search_edge_cases():
    """Test edge cases for KMP search."""
    # Pattern longer than text
    assert kmp_search("ABC", "ABCD") == []
    
    # Pattern at the start of text
    assert kmp_search("ABCDEF", "ABC") == [0]
    
    # Pattern at the end of text
    assert kmp_search("ABCDEF", "DEF") == [3]

def test_kmp_search_error_handling():
    """Test error handling for invalid inputs."""
    # Non-string inputs
    with pytest.raises(TypeError):
        kmp_search(123, "pattern")
    
    with pytest.raises(TypeError):
        kmp_search("text", 456)
    
    # Empty pattern
    with pytest.raises(ValueError):
        kmp_search("text", "")

def test_kmp_search_overlapping_patterns():
    """Test search with overlapping pattern occurrences."""
    # Overlapping pattern
    assert kmp_search("AAAAA", "AA") == [0, 1, 2, 3]

def test_kmp_search_case_sensitive():
    """Test case sensitivity of the search."""
    assert kmp_search("AbCdEfG", "Cd") == []
    assert kmp_search("AbCdEfG", "Cd") != [2]  # Case matters

def test_empty_text():
    """Test searching in an empty text."""
    assert kmp_search("", "pattern") == []
    assert kmp_search("", "") == []