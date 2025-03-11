import os
import tarfile
import pytest
import shutil
import tempfile

from src.create_tar_archive import create_tar_archive


@pytest.fixture
def sample_directory():
    """Create a temporary directory with sample files for testing."""
    temp_dir = tempfile.mkdtemp()
    try:
        # Create some sample files
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('Test content 1')
        with open(os.path.join(temp_dir, 'file2.txt'), 'w') as f:
            f.write('Test content 2')
        yield temp_dir
    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)


def test_create_tar_archive_default(sample_directory):
    """Test creating tar archive with default parameters."""
    archive_path = create_tar_archive(sample_directory)
    
    # Check archive exists
    assert os.path.exists(archive_path)
    assert archive_path.endswith('.tar.gz')
    
    # Verify archive contents
    with tarfile.open(archive_path, 'r:gz') as tar:
        members = tar.getnames()
        assert len(members) > 1  # directory + files
        assert any('file1.txt' in m for m in members)
        assert any('file2.txt' in m for m in members)
    
    # Clean up
    os.remove(archive_path)


def test_create_tar_archive_custom_path(sample_directory):
    """Test creating tar archive with a custom archive path."""
    custom_path = os.path.join(os.path.dirname(sample_directory), 'custom_archive.tar.bz2')
    archive_path = create_tar_archive(sample_directory, 
                                      archive_path=custom_path, 
                                      compression='bz2')
    
    # Check archive exists at specified path
    assert os.path.exists(custom_path)
    assert archive_path == custom_path
    
    # Verify archive contents
    with tarfile.open(custom_path, 'r:bz2') as tar:
        members = tar.getnames()
        assert len(members) > 1
    
    # Clean up
    os.remove(custom_path)


def test_create_tar_archive_invalid_directory():
    """Test creating archive for non-existent directory."""
    with pytest.raises(ValueError, match="does not exist"):
        create_tar_archive('/path/to/nonexistent/directory')


def test_create_tar_archive_not_directory():
    """Test creating archive with a file instead of a directory."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'Test file')
        temp_file_path = temp_file.name
    
    try:
        with pytest.raises(ValueError, match="is not a directory"):
            create_tar_archive(temp_file_path)
    finally:
        os.unlink(temp_file_path)


def test_create_tar_archive_invalid_compression(sample_directory):
    """Test creating archive with invalid compression type."""
    with pytest.raises(ValueError, match="Invalid compression type"):
        create_tar_archive(sample_directory, compression='invalid')


def test_create_tar_archive_compression_types(sample_directory):
    """Test creating archives with different compression types."""
    compression_types = ['gz', 'bz2', 'xz']
    
    for comp_type in compression_types:
        archive_path = create_tar_archive(sample_directory, 
                                          compression=comp_type)
        
        # Check archive exists
        assert os.path.exists(archive_path)
        assert archive_path.endswith(f'.tar.{comp_type}')
        
        # Try to open the archive
        try:
            with tarfile.open(archive_path, f'r:{comp_type}') as tar:
                members = tar.getnames()
                assert len(members) > 1
        except tarfile.TarError:
            pytest.fail(f"Failed to open tar archive with {comp_type} compression")
        
        # Clean up
        os.remove(archive_path)