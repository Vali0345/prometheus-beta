import os
import pytest
import tempfile
import shutil

from src.list_directory_files import list_directory_files

def test_list_directory_files_empty_directory():
    """Test listing files in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        files = list_directory_files(temp_dir)
        assert files == [], "Should return an empty list for an empty directory"

def test_list_directory_files_with_files():
    """Test listing files in a directory with multiple files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        test_files = ['file1.txt', 'file2.txt', 'file3.log']
        for filename in test_files:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        # Create a subdirectory to ensure we only list files
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        
        # List files
        files = list_directory_files(temp_dir)
        
        # Check that only the files are listed, not the directory
        assert set(files) == set(test_files), "Should return only file names"

def test_list_directory_files_nonexistent_directory():
    """Test that FileNotFoundError is raised for a nonexistent directory."""
    with pytest.raises(FileNotFoundError):
        list_directory_files('/path/to/nonexistent/directory')

def test_list_directory_files_not_a_directory():
    """Test that NotADirectoryError is raised when path is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            list_directory_files(temp_file.name)

def test_list_directory_files_special_filenames():
    """Test handling of files with special characters in names."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files with special characters
        special_files = ['file with spaces.txt', 'file@special.log', 'file#hash.py']
        for filename in special_files:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        files = list_directory_files(temp_dir)
        assert set(files) == set(special_files), "Should handle special characters in filenames"