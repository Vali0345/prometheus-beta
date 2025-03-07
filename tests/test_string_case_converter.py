import pytest
from src.string_case_converter import to_kebab_case

def test_basic_string_conversion():
    """Test basic string conversion to kebab case."""
    assert to_kebab_case("Hello World") == "hello-world"

def test_camel_case_conversion():
    """Test conversion of camelCase to kebab-case."""
    assert to_kebab_case("camelCaseString") == "camel-case-string"

def test_pascal_case_conversion():
    """Test conversion of PascalCase to kebab-case."""
    assert to_kebab_case("PascalCaseString") == "pascal-case-string"

def test_snake_case_conversion():
    """Test conversion of snake_case to kebab-case."""
    assert to_kebab_case("snake_case_string") == "snake-case-string"

def test_multiple_spaces():
    """Test conversion of strings with multiple spaces."""
    assert to_kebab_case("multiple   spaces  test") == "multiple-spaces-test"

def test_mixed_case_with_spaces():
    """Test conversion of mixed case string with spaces."""
    assert to_kebab_case("Mixed Case With Spaces") == "mixed-case-with-spaces"

def test_string_with_special_characters():
    """Test conversion of string with special characters."""
    assert to_kebab_case("Hello, World! 123") == "hello-world-123"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_kebab_case("") == ""

def test_single_word():
    """Test conversion of a single word."""
    assert to_kebab_case("Hello") == "hello"

def test_already_kebab_case():
    """Test conversion of an already kebab-case string."""
    assert to_kebab_case("already-kebab-case") == "already-kebab-case"

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_kebab_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        to_kebab_case(None)