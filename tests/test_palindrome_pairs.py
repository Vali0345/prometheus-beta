import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    words = ["bat", "tab", "cat"]
    expected = [(0, 1), (1, 0)]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_complex_palindrome_pairs():
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    expected = [(0, 1), (1, 0), (3, 4), (4, 3)]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_empty_list():
    words = []
    expected = []
    assert find_palindrome_pairs(words) == expected

def test_single_word():
    words = ["hello"]
    expected = []
    assert find_palindrome_pairs(words) == expected

def test_no_palindrome_pairs():
    words = ["red", "green", "blue"]
    expected = []
    assert find_palindrome_pairs(words) == expected

def test_duplicate_words():
    words = ["a", "a"]
    expected = []
    assert find_palindrome_pairs(words) == expected

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