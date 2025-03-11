import os
import pytest
import tempfile
from src.count_directory_files import count_files_in_directory

def test_count_files_in_directory():
    # Create a temporary directory with some files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files
        for i in range(5):
            open(os.path.join(temp_dir, f'file{i}.txt'), 'w').close()
        
        # Verify count
        assert count_files_in_directory(temp_dir) == 5

def test_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        assert count_files_in_directory(temp_dir) == 0

def test_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        count_files_in_directory('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            count_files_in_directory(temp_file.name)

def test_ignore_subdirectories():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files and a subdirectory
        for i in range(3):
            open(os.path.join(temp_dir, f'file{i}.txt'), 'w').close()
        
        # Create a subdirectory with files
        subdir = os.path.join(temp_dir, 'subdir')
        os.makedirs(subdir)
        for i in range(2):
            open(os.path.join(subdir, f'subfile{i}.txt'), 'w').close()
        
        # Verify only top-level files are counted
        assert count_files_in_directory(temp_dir) == 3