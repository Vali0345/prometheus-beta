import pytest
from src.is_anagram import is_anagram

def test_basic_anagrams():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True

def test_case_insensitive():
    assert is_anagram("Astronomer", "Moon starer") == True
    assert is_anagram("RAIL SAFETY", "fairy tales") == True

def test_whitespace_handling():
    assert is_anagram("debit card", "bad credit") == True
    assert is_anagram("   conversation   ", "voices rant on") == True

def test_non_anagrams():
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False

def test_same_letters_different_count():
    assert is_anagram("aab", "aba") == True
    assert is_anagram("aab", "aaa") == False

def test_empty_strings():
    assert is_anagram("", "") == True

def test_single_character():
    assert is_anagram("a", "a") == True
    assert is_anagram("a", "b") == False

def test_non_string_input():
    with pytest.raises(TypeError):
        is_anagram(123, "test")
    
    with pytest.raises(TypeError):
        is_anagram("test", None)
    
    with pytest.raises(TypeError):
        is_anagram([], "test")