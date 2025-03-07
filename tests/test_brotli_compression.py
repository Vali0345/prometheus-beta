import pytest
import brotli
from src.brotli_compression import compress_brotli, decompress_brotli

def test_compress_decompress_string():
    """Test compression and decompression of a string"""
    original = "Hello, World! This is a test of Brotli compression."
    compressed = compress_brotli(original)
    assert isinstance(compressed, bytes)
    assert compressed != original.encode('utf-8')
    
    decompressed = decompress_brotli(compressed)
    assert decompressed.decode('utf-8') == original

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes"""
    original = b"Binary data for compression test"
    compressed = compress_brotli(original)
    assert isinstance(compressed, bytes)
    assert compressed != original
    
    decompressed = decompress_brotli(compressed)
    assert decompressed == original

def test_compression_quality():
    """Test different compression quality levels"""
    data = "Test data for compression quality"
    
    # Test default quality (11)
    compressed_max = compress_brotli(data)
    
    # Test lowest quality
    compressed_min = compress_brotli(data, quality=0)
    
    assert len(compressed_max) < len(compressed_min)
    
    # Verify compression still works
    assert decompress_brotli(compressed_max).decode('utf-8') == data
    assert decompress_brotli(compressed_min).decode('utf-8') == data

def test_invalid_compression_quality():
    """Test handling of invalid compression quality"""
    data = "Test data"
    
    with pytest.raises(ValueError, match="Compression quality must be between 0 and 11"):
        compress_brotli(data, quality=-1)
    
    with pytest.raises(ValueError, match="Compression quality must be between 0 and 11"):
        compress_brotli(data, quality=12)

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError, match="Input must be str or bytes"):
        compress_brotli(123)
    
    with pytest.raises(TypeError, match="Input must be bytes"):
        decompress_brotli("not bytes")

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_str = ""
    empty_bytes = b""
    
    compressed_str = compress_brotli(empty_str)
    compressed_bytes = compress_brotli(empty_bytes)
    
    assert decompress_brotli(compressed_str) == b""
    assert decompress_brotli(compressed_bytes) == b""