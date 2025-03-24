import pytest
from src.fahrenheit_to_celsius import fahrenheit_to_celsius

def test_fahrenheit_to_celsius_standard_conversion():
    """Test standard temperature conversions."""
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_celsius(212) == 100.0
    assert fahrenheit_to_celsius(98.6) == 37.0

def test_fahrenheit_to_celsius_negative():
    """Test conversion of negative temperatures."""
    assert fahrenheit_to_celsius(-40) == -40.0
    assert fahrenheit_to_celsius(-22) == -30.0

def test_fahrenheit_to_celsius_rounding():
    """Test rounding of conversion results."""
    assert fahrenheit_to_celsius(33.8) == 1.0
    assert fahrenheit_to_celsius(50) == 10.0

def test_fahrenheit_to_celsius_type_error():
    """Test that TypeError is raised for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a number"):
        fahrenheit_to_celsius("not a number")
    with pytest.raises(TypeError, match="Input must be a number"):
        fahrenheit_to_celsius(None)
    with pytest.raises(TypeError, match="Input must be a number"):
        fahrenheit_to_celsius([32])

def test_fahrenheit_to_celsius_precision():
    """Test precision of conversion results."""
    assert fahrenheit_to_celsius(77) == 25.0
    assert fahrenheit_to_celsius(87.8) == 31.0