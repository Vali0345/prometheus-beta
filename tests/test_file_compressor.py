import os
import bz2
import pytest
import tempfile
import shutil

from src.file_compressor import compress_file_bzip2


def test_compress_file_bzip2_default_output():
    """Test compression with default output path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file
        input_file = os.path.join(tmpdir, 'test_input.txt')
        with open(input_file, 'wb') as f:
            f.write(b'This is a test file to compress.')

        # Compress the file
        compressed_path = compress_file_bzip2(input_file)

        # Verify compression
        assert os.path.exists(compressed_path)
        assert compressed_path == input_file + '.bz2'
        
        # Verify content can be decompressed
        with bz2.open(compressed_path, 'rb') as f:
            decompressed_content = f.read()
        
        assert decompressed_content == b'This is a test file to compress.'


def test_compress_file_bzip2_custom_output():
    """Test compression with custom output path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_file = os.path.join(tmpdir, 'test_input.txt')
        output_file = os.path.join(tmpdir, 'custom_compressed.bz2')
        
        with open(input_file, 'wb') as f:
            f.write(b'Another test file to compress.')

        compressed_path = compress_file_bzip2(input_file, output_file)

        assert os.path.exists(compressed_path)
        assert compressed_path == output_file
        
        with bz2.open(compressed_path, 'rb') as f:
            decompressed_content = f.read()
        
        assert decompressed_content == b'Another test file to compress.'


def test_compress_file_bzip2_nonexistent_file():
    """Test compression of a nonexistent file raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        nonexistent_file = os.path.join(tmpdir, 'does_not_exist.txt')
        
        with pytest.raises(FileNotFoundError):
            compress_file_bzip2(nonexistent_file)


def test_compress_file_bzip2_directory():
    """Test compression of a directory raises IsADirectoryError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(IsADirectoryError):
            compress_file_bzip2(tmpdir)


def test_compress_file_bzip2_large_file():
    """Test compression of a large file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        large_file = os.path.join(tmpdir, 'large_test.txt')
        
        # Create a large file
        with open(large_file, 'wb') as f:
            f.write(b'0' * (1024 * 1024))  # 1MB of zeros

        compressed_path = compress_file_bzip2(large_file)

        assert os.path.exists(compressed_path)
        assert os.path.getsize(compressed_path) < os.path.getsize(large_file)
        
        # Verify decompression
        with bz2.open(compressed_path, 'rb') as f:
            decompressed_content = f.read()
        
        assert len(decompressed_content) == 1024 * 1024
        assert decompressed_content == b'0' * (1024 * 1024)