import pytest
from src.reverse_word_order import reverse_word_order

def test_basic_word_reversal():
    """Test basic word order reversal."""
    assert reverse_word_order("Hello World") == "World Hello"

def test_single_word():
    """Test single word input remains unchanged."""
    assert reverse_word_order("Hello") == "Hello"

def test_empty_string():
    """Test empty string input."""
    assert reverse_word_order("") == ""

def test_multiple_words():
    """Test reversal of multiple words."""
    assert reverse_word_order("Python is awesome") == "awesome is Python"

def test_input_with_punctuation():
    """Test reversal while preserving punctuation."""
    assert reverse_word_order("Hello, World!") == "World! Hello,"

def test_mixed_case():
    """Test preservation of original case."""
    assert reverse_word_order("Python Is AWESOME") == "AWESOME Is Python"

def test_extra_whitespace():
    """Test handling of extra whitespace."""
    assert reverse_word_order("  Hello   World  ") == "World Hello"

def test_numeric_words():
    """Test reversal with numeric words."""
    assert reverse_word_order("10 20 30") == "30 20 10"