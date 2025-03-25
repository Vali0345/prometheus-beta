"""
LZJB Compression Algorithm Implementation

This module provides a Python implementation of the LZJB compression algorithm.
LZJB is a fast compression algorithm developed by Jeff Bonwick at Sun Microsystems.

References:
- Original LZJB algorithm design
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
        # Try to find a match in previous window
        best_length = 0
        best_offset = 0
        
        # Define search window
        search_start = max(0, input_idx - 1024)
        search_end = input_idx
        
        for offset in range(search_start, search_end):
            match_length = 0
            max_match = min(8, input_len - input_idx)  # Limit match length
            
            while (match_length < max_match and 
                   data[offset + match_length] == data[input_idx + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = input_idx - offset
        
        # Encode match or literal
        if best_length > 2:
            # Match encoding: use top 13 bits for offset, bottom 3 for length
            token = ((best_offset & 0x1FFF) << 3) | ((best_length - 3) & 0x07)
            output.append(token & 0xFF)
            input_idx += best_length
        else:
            # Literal encoding
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
            # Decode match token
            offset = (token >> 3) & 0x1FFF
            length = (token & 0x07) + 3
            
            # Reconstruct match
            match_start = len(output) - offset
            
            # Copy matched segment
            for _ in range(length):
                if match_start >= 0 and match_start < len(output):
                    output.append(output[match_start])
                    match_start += 1
                else:
                    # Handle edge cases with repeated last element
                    if output:
                        output.append(output[-1])
                    else:
                        # Fallback to zero in extremely unlikely case of empty output
                        output.append(0)
    
    return output