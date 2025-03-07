import brotli
from typing import Union

def compress_brotli(data: Union[str, bytes], quality: int = 11) -> bytes:
    """
    Compress data using Brotli compression algorithm.

    Args:
        data (str or bytes): The input data to compress. 
            If str, it will be encoded to UTF-8 bytes.
        quality (int, optional): Compression quality level. 
            Range is 0-11, where 0 is fastest, 11 is most compressed. 
            Defaults to 11 (maximum compression).

    Returns:
        bytes: Brotli compressed data.

    Raises:
        ValueError: If quality is not between 0 and 11.
        TypeError: If data is not str or bytes.
    """
    # Validate compression quality
    if not 0 <= quality <= 11:
        raise ValueError("Compression quality must be between 0 and 11")

    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise TypeError("Input must be str or bytes")

    # Compress using brotli
    return brotli.compress(data, quality)

def decompress_brotli(compressed_data: bytes) -> bytes:
    """
    Decompress Brotli compressed data.

    Args:
        compressed_data (bytes): Brotli compressed data.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        brotli.error: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    # Decompress using brotli
    return brotli.decompress(compressed_data)