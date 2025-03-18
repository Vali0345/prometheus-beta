import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert len(result) == 2
    assert (0, 1) in result
    assert (1, 0) in result

def test_complex_palindrome_pairs():
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    expected_pairs = {(0, 1), (1, 0), (3, 4), (4, 3)}
    assert set(result) == expected_pairs

def test_empty_list():
    words = []
    assert find_palindrome_pairs(words) == []

def test_single_word():
    words = ["hello"]
    assert find_palindrome_pairs(words) == []

def test_no_palindrome_pairs():
    words = ["red", "green", "blue"]
    assert find_palindrome_pairs(words) == []

def test_duplicate_words():
    words = ["a", "a"]
    assert find_palindrome_pairs(words) == []

@pytest.mark.parametrize("words", [
    ["racecar", "level"],
    ["a", "b", "c"],
    ["programming", "mingogram"]
])
def test_various_input_scenarios(words):
    # Ensure the function returns a valid list of pairs or an empty list
    result = find_palindrome_pairs(words)
    assert isinstance(result, list)
    assert all(isinstance(pair, tuple) and len(pair) == 2 for pair in result)