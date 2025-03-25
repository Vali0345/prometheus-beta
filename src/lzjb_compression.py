"""
LZJB Compression Algorithm Implementation

This module provides a Python implementation of the LZJB compression algorithm.
LZJB is a fast compression algorithm that provides a good balance between 
compression speed and compression ratio.

References:
- Original LZJB algorithm by Jeff Bonwick (Sun Microsystems)
"""

def compress(data):
    """
    Compress input data using the LZJB compression algorithm.
    
    Args:
        data (bytes or bytearray): Input data to be compressed
    
    Returns:
        bytearray: Compressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Initialize compression variables
    output = bytearray()
    input_len = len(data)
    input_idx = 0
    
    while input_idx < input_len:
        # Look for the longest match in the previous window
        best_length = 0
        best_offset = 0
        
        # Define search window (limit lookback to prevent excessive memory usage)
        window_start = max(0, input_idx - 1024)
        window_end = input_idx
        
        # Search for the longest match in the window
        for offset in range(window_start, window_end):
            match_length = 0
            while (input_idx + match_length < input_len and 
                   data[offset + match_length] == data[input_idx + match_length] and 
                   match_length < 255):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = input_idx - offset
        
        # Encode the match or literal
        if best_length > 2:
            # Encode match: [offset bits][length bits]
            token = ((best_offset << 3) | (best_length - 3)) | 0x20
            output.append(token)
            input_idx += best_length
        else:
            # Encode literal
            output.append(data[input_idx])
            input_idx += 1
    
    return output

def decompress(compressed_data):
    """
    Decompress data compressed with the LZJB compression algorithm.
    
    Args:
        compressed_data (bytes or bytearray): Compressed input data
    
    Returns:
        bytearray: Decompressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    # Initialize decompression variables
    output = bytearray()
    input_idx = 0
    input_len = len(compressed_data)
    
    while input_idx < input_len:
        token = compressed_data[input_idx]
        input_idx += 1
        
        if token < 32:  # Literal
            output.append(token)
        else:
            # Decode match
            offset = (token >> 3) & 0x1FFF
            length = (token & 0x07) + 3
            
            # Reconstruct match
            start = max(0, len(output) - offset)
            for _ in range(length):
                if start < len(output):
                    output.append(output[start])
                    start += 1
                else:
                    # If start is beyond current output length, cycle through previous characters
                    output.append(output[start % len(output)])
    
    return output