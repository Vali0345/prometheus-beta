import pytest
import lzma
import sys
from src.lzma2_compression import lzma2_compress, lzma2_decompress

def test_lzma2_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, world! This is a test of LZMA2 compression."
    compressed = lzma2_compress(original_data)
    assert compressed != original_data
    
    # For small inputs, compressed size might be larger due to overhead
    # So we'll just assert that compression works without raising errors
    decompressed = lzma2_decompress(compressed)
    assert decompressed == original_data

def test_lzma2_compression_string():
    """Test compression with string input"""
    original_data = "Python is awesome! 🐍"
    compressed = lzma2_compress(original_data)
    assert compressed != original_data.encode('utf-8')
    
    decompressed = lzma2_decompress(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_lzma2_compression_large_data():
    """Test compression with larger data"""
    original_data = b"a" * 10000
    compressed = lzma2_compress(original_data)
    assert len(compressed) < len(original_data)
    
    decompressed = lzma2_decompress(compressed)
    assert decompressed == original_data

def test_lzma2_error_handling():
    """Test error handling for invalid inputs"""
    # Test invalid input type
    with pytest.raises(TypeError):
        lzma2_compress(123)
    
    with pytest.raises(TypeError):
        lzma2_decompress(123)
    
    # Test empty input
    with pytest.raises(ValueError):
        lzma2_compress(b"")
    
    with pytest.raises(ValueError):
        lzma2_decompress(b"")

def test_lzma2_decompress_invalid_data():
    """Test decompression with invalid compressed data"""
    invalid_data = b"This is not valid compressed data"
    with pytest.raises(ValueError):
        lzma2_decompress(invalid_data)

def test_lzma2_reversibility():
    """Ensure compression and decompression are fully reversible"""
    test_cases = [
        b"Short text",
        "Unicode text with emojis 🚀🌍",
        b"\x00\x01\x02\x03\x04" * 100,  # Binary data
        "こんにちは"  # Japanese text
    ]
    
    for original_data in test_cases:
        # Compress string or bytes
        if isinstance(original_data, str):
            input_data = original_data
        else:
            input_data = original_data
        
        compressed = lzma2_compress(input_data)
        decompressed = lzma2_decompress(compressed)
        
        # Ensure decompressed matches original
        if isinstance(original_data, str):
            assert decompressed == original_data.encode('utf-8')
        else:
            assert decompressed == original_data