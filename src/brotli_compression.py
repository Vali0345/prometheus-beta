import brotli
from typing import Union

def compress_brotli(data: Union[str, bytes], quality: int = 11, mode: int = 0) -> bytes:
    """
    Compress data using Brotli compression algorithm.

    Args:
        data (str or bytes): The input data to compress. 
            If str, it will be encoded to UTF-8 bytes.
        quality (int, optional): Compression quality level. 
            Range is 0-11, where 0 is fastest, 11 is most compressed. 
            Defaults to 11 (maximum compression).
        mode (int, optional): Compression mode. 
            0: MODE_GENERIC (default)
            1: MODE_TEXT (for UTF-8 text)
            2: MODE_FONT (for WOFF 2.0)
            Defaults to 0.

    Returns:
        bytes: Brotli compressed data.

    Raises:
        ValueError: If quality is not between 0 and 11 or mode is invalid.
        TypeError: If data is not str or bytes.
    """
    # Validate compression quality
    if not 0 <= quality <= 11:
        raise ValueError("Compression quality must be between 0 and 11")

    # Validate mode
    if mode not in [0, 1, 2]:
        raise ValueError("Invalid compression mode. Must be 0, 1, or 2.")

    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise TypeError("Input must be str or bytes")

    # Compress using brotli
    return brotli.compress(data, mode=mode, quality=quality)

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