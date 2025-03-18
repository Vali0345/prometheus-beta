import pytest
from src.sponge_case import to_sponge_case

def test_basic_sponge_case():
    """Test basic sponge case conversion."""
    assert to_sponge_case("hello") == 'hElLo'
    assert to_sponge_case("world") == 'wOrLd'

def test_uppercase_input():
    """Test conversion of uppercase input."""
    assert to_sponge_case("HELLO") == 'hElLo'

def test_mixed_case_input():
    """Test conversion of mixed case input."""
    assert to_sponge_case("HeLLo") == 'hElLo'

def test_empty_string():
    """Test empty string input."""
    assert to_sponge_case("") == ''

def test_single_character():
    """Test single character input."""
    assert to_sponge_case("a") == 'a'
    assert to_sponge_case("B") == 'b'

def test_special_characters():
    """Test input with special characters."""
    assert to_sponge_case("hello, world!") == 'hElLo, WoRlD!'

def test_numbers():
    """Test input with numbers."""
    assert to_sponge_case("hello123") == 'hElLo123'

def test_invalid_input_type():
    """Test invalid input type raises TypeError."""
    with pytest.raises(TypeError):
        to_sponge_case(123)
    
    with pytest.raises(TypeError):
        to_sponge_case(None)