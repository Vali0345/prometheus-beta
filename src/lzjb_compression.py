"""
LZJB Compression Algorithm Implementation

A Python implementation of the LZJB compression algorithm,
inspired by the original design by Jeff Bonwick.

Key characteristics:
- Fast compression and decompression
- Lightweight matching algorithm
- Works well with small to medium-sized inputs
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
    
    # Compression parameters
    input_len = len(data)
    output = bytearray()
    input_idx = 0
    
    while input_idx < input_len:
        # Search backwards for matching substring
        best_length = 0
        best_offset = 0
        
        # Look back up to 1024 bytes
        window_start = max(0, input_idx - 1024)
        window_end = input_idx
        
        for offset in range(window_start, window_end):
            # Compute match length
            match_length = 0
            max_length = min(8, input_len - input_idx)
            
            while (match_length < max_length and 
                   data[offset + match_length] == data[input_idx + match_length]):
                match_length += 1
            
            # Update best match
            if match_length > best_length:
                best_length = match_length
                best_offset = input_idx - offset
        
        # Encode match or literal
        if best_length > 2:
            # Encode match: [offset bits][length bits]
            token = ((best_offset & 0x1FFF) << 3) | ((best_length - 3) & 0x07)
            output.append(token & 0xFF)
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
    
    output = bytearray()
    input_idx = 0
    input_len = len(compressed_data)
    
    while input_idx < input_len:
        token = compressed_data[input_idx]
        input_idx += 1
        
        if token < 32:  # Literal
            output.append(token)
        else:
            # Match decoding
            offset = (token >> 3) & 0x1FFF  # Top 13 bits
            length = (token & 0x07) + 3     # Bottom 3 bits
            
            # Reconstruct match carefully
            match_start = len(output) - offset
            
            # Validate match start position
            if 0 <= match_start < len(output):
                for _ in range(length):
                    # Ensure we can safely copy
                    output.append(output[match_start])
                    match_start += 1
            else:
                # Fallback for edge cases
                for _ in range(length):
                    output.append(output[-1] if output else 0)
    
    return output