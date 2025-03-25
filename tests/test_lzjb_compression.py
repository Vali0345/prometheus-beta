"""
Unit tests for LZJB compression and decompression functions.
"""

import pytest
import random
import string
from src.lzjb_compression import compress, decompress

def test_compress_decompress_simple_string():
    """Test basic compression and decompression of a simple string."""
    original = b"hello world hello world"
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert len(decompressed) == len(original)
    assert all(a == b for a, b in zip(original, decompressed))

def test_compress_decompress_random_bytes():
    """Test compression and decompression of random bytes."""
    # Generate random bytes
    random.seed(42)  # For reproducibility
    original = bytes(random.getrandbits(8) for _ in range(1000))
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert len(decompressed) == len(original)
    assert all(a == b for a, b in zip(original, decompressed))

def test_compress_decompress_repeated_pattern():
    """Test compression of data with repeated patterns."""
    original = b"abcabcabcabcabcabcabcabc" * 10
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert len(decompressed) == len(original)
    assert all(a == b for a, b in zip(original, decompressed))

def test_compression_ratio():
    """Basic test to ensure some level of compression."""
    original = b"hello world " * 100
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert len(decompressed) == len(original)
    assert all(a == b for a, b in zip(original, decompressed))
    assert len(compressed) < len(original)

def test_large_input():
    """Test compression and decompression of a large input."""
    # Generate a larger random input
    random.seed(123)  # For reproducibility
    original = bytes(random.getrandbits(8) for _ in range(10000))
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert len(decompressed) == len(original)
    assert all(a == b for a, b in zip(original, decompressed))

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError):
        compress(b"")
    with pytest.raises(ValueError):
        decompress(b"")

def test_invalid_input_type_raises_error():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError):
        compress("not bytes")
    with pytest.raises(TypeError):
        decompress("not bytes")

def test_edge_case_single_byte():
    """Test compression and decompression of a single byte."""
    original = b"a"
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert len(decompressed) == len(original)
    assert all(a == b for a, b in zip(original, decompressed))