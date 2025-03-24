"""
Unit tests for the file_writer module.
"""

import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file_success(tmp_path):
    """
    Test successful writing of a string to a file.
    """
    # Create a temporary file path
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, World!"
    
    # Write the string to the file
    write_string_to_file(str(test_file), test_content)
    
    # Verify the file contents
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == test_content

def test_write_string_to_file_empty_string(tmp_path):
    """
    Test writing an empty string to a file.
    """
    test_file = tmp_path / "empty_file.txt"
    test_content = ""
    
    write_string_to_file(str(test_file), test_content)
    
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == ""

def test_write_string_to_file_invalid_path():
    """
    Test error handling for invalid file path.
    """
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("", "content")

def test_write_string_to_file_invalid_types():
    """
    Test error handling for invalid input types.
    """
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "content")
    
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("test.txt", 456)

def test_write_string_to_file_overwrite(tmp_path):
    """
    Test that writing to an existing file overwrites its contents.
    """
    test_file = tmp_path / "overwrite_file.txt"
    
    # Write initial content
    write_string_to_file(str(test_file), "Initial content")
    
    # Overwrite the content
    new_content = "New content"
    write_string_to_file(str(test_file), new_content)
    
    # Verify the file contains only the new content
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == new_content