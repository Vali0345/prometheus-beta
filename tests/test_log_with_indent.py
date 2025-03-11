"""
Tests for the log_with_indent function.
"""

import pytest
from src.log_with_indent import log_with_indent

def test_basic_indentation():
    """Test basic indentation with default space."""
    message = "Hello\nWorld"
    expected = "    Hello\n    World"
    assert log_with_indent(message, indent_level=1) == expected

def test_different_indent_char():
    """Test indentation with a different character."""
    message = "Hello\nWorld"
    expected = "----Hello\n----World"
    assert log_with_indent(message, indent_level=1, indent_char='-') == expected

def test_zero_indentation():
    """Test zero indentation."""
    message = "Hello\nWorld"
    assert log_with_indent(message) == message

def test_multiple_indent_levels():
    """Test multiple indentation levels."""
    message = "Hello\nWorld"
    expected = "        Hello\n        World"
    assert log_with_indent(message, indent_level=2) == expected

def test_empty_string():
    """Test empty string indentation."""
    assert log_with_indent("") == ""

def test_invalid_message_type():
    """Test raising TypeError for non-string message."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_indent(123)

def test_invalid_indent_level_type():
    """Test raising TypeError for non-integer indent level."""
    with pytest.raises(TypeError, match="Indent level must be an integer"):
        log_with_indent("Hello", indent_level="1")

def test_negative_indent_level():
    """Test raising ValueError for negative indent level."""
    with pytest.raises(ValueError, match="Indent level cannot be negative"):
        log_with_indent("Hello", indent_level=-1)

def test_invalid_indent_char():
    """Test raising ValueError for multi-character indent character."""
    with pytest.raises(ValueError, match="Indent character must be a single character"):
        log_with_indent("Hello", indent_char="  ")