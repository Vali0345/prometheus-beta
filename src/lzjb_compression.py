"""
LZJB-inspired Compression Algorithm

A lightweight compression implementation designed to showcase 
basic compression techniques.
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
        # Define window for matching
        window_start = max(0, input_idx - 1024)
        best_match_length = 0
        best_match_offset = 0
        
        # Search for longest match
        for offset in range(window_start, input_idx):
            # Compute match length 
            match_length = 0
            max_match = min(8, input_len - input_idx)
            
            while (match_length < max_match and 
                   data[offset + match_length] == data[input_idx + match_length]):
                match_length += 1
            
            # Update best match if longer
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = input_idx - offset
        
        # Encode match or literal
        if best_match_length > 2:
            # Match token
            token = ((best_match_offset & 0x1FFF) << 3) | ((best_match_length - 3) & 0x07)
            output.append(token & 0xFF)
            input_idx += best_match_length
        else:
            # Literal 
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
    
    # Output buffer
    output = bytearray()
    input_idx = 0
    input_len = len(compressed_data)
    
    while input_idx < input_len:
        token = compressed_data[input_idx]
        input_idx += 1
        
        if token < 32:  # Literal byte
            output.append(token)
        else:
            # Match token decoding
            dist = (token >> 3) & 0x1FFF
            length = (token & 0x07) + 3
            
            # Match reconstruction 
            start_pos = len(output) - dist
            for _ in range(length):
                if 0 <= start_pos < len(output):
                    output.append(output[start_pos])
                    start_pos += 1
                else:
                    # Handle edge cases 
                    output.append(output[-1] if output else 0)
    
    return output