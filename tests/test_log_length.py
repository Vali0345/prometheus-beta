import pytest
import logging
from src.log_length import log_length

def test_log_length_string(caplog):
    """Test logging length of a string."""
    caplog.set_level(logging.INFO)
    result = log_length("hello")
    assert result == 5
    assert "Length of input: 5" in caplog.text

def test_log_length_list(caplog):
    """Test logging length of a list."""
    caplog.set_level(logging.INFO)
    result = log_length([1, 2, 3, 4])
    assert result == 4
    assert "Length of input: 4" in caplog.text

def test_log_length_tuple(caplog):
    """Test logging length of a tuple."""
    caplog.set_level(logging.INFO)
    result = log_length((1, 2, 3))
    assert result == 3
    assert "Length of input: 3" in caplog.text

def test_log_length_empty(caplog):
    """Test logging length of an empty string/list/tuple."""
    caplog.set_level(logging.INFO)
    result = log_length("")
    assert result == 0
    assert "Length of input: 0" in caplog.text

def test_log_length_invalid_type():
    """Test raising TypeError for invalid input type."""
    with pytest.raises(TypeError, match="Input must be a string, list, or tuple"):
        log_length(123)

def test_log_length_complex_inputs(caplog):
    """Test logging length of more complex inputs."""
    caplog.set_level(logging.INFO)
    # String with spaces
    result = log_length("hello world")
    assert result == 11
    assert "Length of input: 11" in caplog.text

    # List with mixed types
    result = log_length([1, "two", None, [4]])
    assert result == 4
    assert "Length of input: 4" in caplog.text