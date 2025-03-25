"""
Simple LZJB-inspired Compression Algorithm

A simplified implementation focusing on core compression principles.
"""

def compress(data):
    """
    Compress input data using a lightweight compression approach.
    
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
    
    output = bytearray()
    input_len = len(data)
    input_idx = 0
    
    while input_idx < input_len:
        # Look for matching sequences
        match_found = False
        
        # Define search window
        window_start = max(0, input_idx - 1024)
        
        for offset in range(window_start, input_idx):
            # Try to find the longest match
            match_length = 0
            max_match = min(8, input_len - input_idx)
            
            while (match_length < max_match and 
                   data[offset + match_length] == data[input_idx + match_length]):
                match_length += 1
            
            # If a decent match is found
            if match_length > 2:
                # Encode match
                distance = input_idx - offset
                token = ((distance & 0x1FFF) << 3) | ((match_length - 3) & 0x07)
                output.append(token & 0xFF)
                input_idx += match_length
                match_found = True
                break
        
        # If no match found, encode literal
        if not match_found:
            output.append(data[input_idx])
            input_idx += 1
    
    return output

def decompress(compressed_data):
    """
    Decompress data compressed by the compression function.
    
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
        
        # Literal byte
        if token < 32:
            output.append(token)
        else:
            # Match token
            distance = (token >> 3) & 0x1FFF
            length = (token & 0x07) + 3
            
            # Reconstruct match
            match_start = len(output) - distance
            
            # Handle match reconstruction carefully
            for _ in range(length):
                if 0 <= match_start < len(output):
                    output.append(output[match_start])
                    match_start += 1
                else:
                    # Fallback for edge cases
                    output.append(output[-1] if output else 0)
    
    return output