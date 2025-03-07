import os
import pytest
import stat
from src.file_permissions import change_file_permissions

def test_change_file_permissions_success(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test.txt"
    test_file.write_text("Test content")
    
    # Change permissions
    result = change_file_permissions(str(test_file), 0o755)
    assert result is True
    
    # Check if permissions were actually changed
    file_stat = os.stat(str(test_file))
    assert file_stat.st_mode & 0o777 == 0o755

def test_change_file_permissions_invalid_path():
    with pytest.raises(FileNotFoundError):
        change_file_permissions("/non/existent/file.txt", 0o644)

def test_change_file_permissions_invalid_permissions(tmp_path):
    test_file = tmp_path / "invalid_perms.txt"
    test_file.write_text("Test content")
    with pytest.raises(ValueError):
        change_file_permissions(str(test_file), 0o1000)  # Invalid permissions

def test_change_file_permissions_invalid_type():
    with pytest.raises(TypeError):
        change_file_permissions(123, 0o644)  # Invalid file path type
    
    with pytest.raises(TypeError):
        change_file_permissions("/tmp/test.txt", "644")  # Invalid permissions type

def test_minimum_and_maximum_permissions(tmp_path):
    # Test minimum permissions (no access for anyone)
    test_file1 = tmp_path / "test1.txt"
    test_file1.write_text("Test content")
    change_file_permissions(str(test_file1), 0o000)
    assert os.stat(str(test_file1)).st_mode & 0o777 == 0o000

    # Test maximum permissions (full access for everyone)
    test_file2 = tmp_path / "test2.txt"
    test_file2.write_text("Test content")
    change_file_permissions(str(test_file2), 0o777)
    assert os.stat(str(test_file2)).st_mode & 0o777 == 0o777