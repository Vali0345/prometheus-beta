"""
LZJB Compression Algorithm Implementation

A simplified implementation of the LZJB compression algorithm.
"""

def compress(data):
    """
    Compress input data.
    
    Args:
        data (bytes or bytearray): Input data to compress
    
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
    
    # Output buffer
    output = bytearray()
    input_len = len(data)
    input_idx = 0
    
    while input_idx < input_len:
        # Find longest matching substring
        best_length = 0
        best_offset = 0
        
        # Look back in previous window
        window_start = max(0, input_idx - 1024)
        window_end = input_idx
        
        for offset in range(window_start, window_end):
            match_length = 0
            while (input_idx + match_length < input_len and 
                   data[offset + match_length] == data[input_idx + match_length] and 
                   match_length < 8):
                match_length += 1
            
            # Update best match
            if match_length > best_length:
                best_length = match_length
                best_offset = input_idx - offset
        
        # Encode match or literal
        if best_length > 2:
            # Encode match token
            token = (best_offset << 3) | (best_length - 3)
            output.append(token & 0xFF)
            input_idx += best_length
        else:
            # Encode literal
            output.append(data[input_idx])
            input_idx += 1
    
    return output

def decompress(compressed_data):
    """
    Decompress data.
    
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
    
    # Output buffer
    output = bytearray()
    input_idx = 0
    input_len = len(compressed_data)
    
    while input_idx < input_len:
        token = compressed_data[input_idx]
        input_idx += 1
        
        # Literal 
        if token < 32:
            output.append(token)
        else:
            # Match token
            offset = (token >> 3) & 0x1FFF
            length = (token & 0x07) + 3
            
            # Handle match 
            match_start = len(output) - offset
            for _ in range(length):
                if 0 <= match_start < len(output):
                    output.append(output[match_start])
                    match_start += 1
                else:
                    # Fallback for edge cases
                    output.append(output[-1] if output else 0)
    
    return output