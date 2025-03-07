"""
Test suite for LZRW compression algorithm implementation.
"""

import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzrw_compression import compress, decompress

def test_compress_decompress_simple_string():
    """Test basic compression and decompression of a simple string."""
    original = "hello world"
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes."""
    original = b'\x00\x01\x02\x03\x04\x05'
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed == original

def test_compress_decompress_repeated_pattern():
    """Test compression of a repeated pattern."""
    original = "abcabcabcabc" * 10
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_compress_empty_input():
    """Test compression and decompression of empty input."""
    original = ""
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_compress_large_input():
    """Test compression and decompression of a large input."""
    original = "x" * 1000 + "y" * 1000
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_invalid_input_type():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        compress(123)
    
    with pytest.raises(TypeError):
        decompress(123)

def test_compression_ratio():
    """Verify that compression provides some reduction for repetitive data."""
    original = "abcabcabcabc" * 100
    compressed = compress(original)
    assert len(compressed) < len(original)

def test_symmetric_compression():
    """Ensure symmetric compression and decompression."""
    test_cases = [
        "hello world",
        "repeated repeated repeated",
        b'\x00\x01\x02\x03\x04\x05',
        "x" * 1000,
    ]
    
    for original in test_cases:
        compressed = compress(original)
        decompressed = decompress(compressed)
        
        # Convert to consistent type for comparison
        if isinstance(original, str):
            assert decompressed.decode('utf-8') == original
        else:
            assert decompressed == original