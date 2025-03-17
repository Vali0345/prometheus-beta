import os
import pytest
import tempfile
import shutil

from src.largest_file_finder import find_largest_file

def test_find_largest_file_basic():
    """Test finding the largest file in a simple directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files with different sizes
        with open(os.path.join(tmpdir, 'small.txt'), 'w') as f:
            f.write('small')
        
        with open(os.path.join(tmpdir, 'large.txt'), 'w') as f:
            f.write('large' * 100)
        
        # Find largest file
        largest = find_largest_file(tmpdir)
        assert largest == os.path.join(tmpdir, 'large.txt')

def test_find_largest_file_nested():
    """Test finding the largest file in nested directories."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create nested directories with files
        os.makedirs(os.path.join(tmpdir, 'subdir1'))
        os.makedirs(os.path.join(tmpdir, 'subdir2'))
        
        with open(os.path.join(tmpdir, 'small.txt'), 'w') as f:
            f.write('small')
        
        with open(os.path.join(tmpdir, 'subdir1', 'medium.txt'), 'w') as f:
            f.write('medium' * 50)
        
        with open(os.path.join(tmpdir, 'subdir2', 'large.txt'), 'w') as f:
            f.write('large' * 100)
        
        # Find largest file
        largest = find_largest_file(tmpdir)
        assert largest == os.path.join(tmpdir, 'subdir2', 'large.txt')

def test_find_largest_file_empty_directory():
    """Test behavior with an empty directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        largest = find_largest_file(tmpdir)
        assert largest is None

def test_find_largest_file_invalid_directory():
    """Test error handling for invalid directory paths."""
    with pytest.raises(ValueError, match="Directory does not exist"):
        find_largest_file('/path/to/nonexistent/directory')
    
    with pytest.raises(ValueError, match="Provided path is not a directory"):
        # Create a temporary file and try to use it as a directory
        with tempfile.NamedTemporaryFile() as tmpfile:
            find_largest_file(tmpfile.name)

def test_find_largest_file_with_permission_errors():
    """Test handling of files with permission errors."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create files
        with open(os.path.join(tmpdir, 'small.txt'), 'w') as f:
            f.write('small')
        
        with open(os.path.join(tmpdir, 'large.txt'), 'w') as f:
            f.write('large' * 100)
        
        # Make a file unreadable (on systems that support this)
        try:
            os.chmod(os.path.join(tmpdir, 'small.txt'), 0o000)
        except PermissionError:
            # If changing permissions isn't possible, skip this specific test
            pytest.skip("Cannot modify file permissions")
        
        # Find largest file
        largest = find_largest_file(tmpdir)
        assert largest == os.path.join(tmpdir, 'large.txt')
        
        # Restore permissions
        os.chmod(os.path.join(tmpdir, 'small.txt'), 0o644)