import lzma
import io

def lzma2_compress(input_data):
    """
    Compress input data using LZMA2 compression algorithm.

    Args:
        input_data (bytes or str): Data to be compressed.
            If str is provided, it will be encoded to UTF-8 bytes.

    Returns:
        bytes: Compressed data using LZMA2 compression.

    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate input type
    if not isinstance(input_data, (bytes, str)):
        raise TypeError("Input must be bytes or str")
    
    # Convert str to bytes if necessary
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Check for empty input
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Compress using LZMA2 (LZMA container)
    compressed = lzma.compress(input_data, preset=lzma.PRESET_DEFAULT)
    
    return compressed

def lzma2_decompress(compressed_data):
    """
    Decompress data compressed with LZMA2 compression algorithm.

    Args:
        compressed_data (bytes): Data to be decompressed.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty or cannot be decompressed.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Check for empty input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    try:
        # Decompress using LZMA2
        decompressed = lzma.decompress(compressed_data)
        return decompressed
    except lzma.LZMAError as e:
        raise ValueError(f"Decompression failed: {str(e)}")