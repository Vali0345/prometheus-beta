import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_initialization():
    """Test basic initialization of Suffix Tree."""
    text = "banana"
    suffix_tree = SuffixTree(text)
    assert suffix_tree.text == "banana$"

def test_suffix_tree_search():
    """Test pattern searching in Suffix Tree."""
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    # Test existing patterns
    assert suffix_tree.search("banana") == True
    assert suffix_tree.search("ana") == True
    assert suffix_tree.search("ban") == True
    
    # Test non-existing patterns
    assert suffix_tree.search("ananas") == False
    assert suffix_tree.search("bananaa") == False

def test_suffix_tree_all_occurrences():
    """Test finding all occurrences of a pattern."""
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    # Test pattern with multiple occurrences
    assert suffix_tree.all_occurrences("ana") == [1, 3]
    
    # Test pattern with single occurrence
    assert suffix_tree.all_occurrences("ban") == [0]
    
    # Test pattern not in text
    assert suffix_tree.all_occurrences("nanas") == []

def test_suffix_tree_invalid_input():
    """Test error handling for invalid inputs."""
    # Test empty string
    with pytest.raises(ValueError):
        SuffixTree("")
    
    # Test non-string input
    with pytest.raises(ValueError):
        SuffixTree(123)
    
    # Test search with invalid patterns
    suffix_tree = SuffixTree("hello")
    with pytest.raises(ValueError):
        suffix_tree.search("")
    
    with pytest.raises(ValueError):
        suffix_tree.search(123)
    
    with pytest.raises(ValueError):
        suffix_tree.all_occurrences("")
    
    with pytest.raises(ValueError):
        suffix_tree.all_occurrences(123)

def test_long_text_search():
    """Test Suffix Tree with a longer text."""
    text = "abracadabra is a magical incantation"
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.search("abra") == True
    assert suffix_tree.search("magical") == True
    assert suffix_tree.search("unicorn") == False
    
    # Test specific occurrences
    occurrences = suffix_tree.all_occurrences("abra")
    assert len(occurrences) > 1
    assert 0 in occurrences
    assert 7 in occurrences