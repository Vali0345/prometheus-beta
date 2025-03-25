"""
Lightweight LZJB-Inspired Compression Algorithm

A basic implementation demonstrating compression principles.
"""

def compress(data):
    """
    Compress input data using a simple matching algorithm.
    
    Args:
        data (bytes or bytearray): Input data to compress
    
    Returns:
        bytes: Compressed data
    
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
        # Search for matching substrings
        best_length = 0
        best_offset = 0
        
        # Look back in a compressed window
        window_start = max(0, input_idx - 1024)
        
        for offset in range(window_start, input_idx):
            match_length = 0
            max_match = min(8, input_len - input_idx)
            
            while (match_length < max_match and 
                   data[offset + match_length] == data[input_idx + match_length]):
                match_length += 1
            
            # Update best match
            if match_length > best_length:
                best_length = match_length
                best_offset = input_idx - offset
        
        # Encode match or literal
        if best_length > 2:
            # Match token
            token = ((best_offset & 0x1FFF) << 3) | ((best_length - 3) & 0x07)
            output.append(token & 0xFF)
            input_idx += best_length
        else:
            # Literal
            output.append(data[input_idx])
            input_idx += 1
    
    return bytes(output)

def decompress(compressed_data):
    """
    Decompress data using a matching reconstruction strategy.
    
    Args:
        compressed_data (bytes or bytearray): Compressed input data
    
    Returns:
        bytes: Decompressed data
    
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
            # Match token decoding
            offset = (token >> 3) & 0x1FFF
            length = (token & 0x07) + 3
            
            # Match reconstruction
            start = len(output) - offset
            match = []
            
            for _ in range(length):
                if 0 <= start < len(output):
                    match.append(output[start])
                    start += 1
                else:
                    # Use last output byte or 0
                    match.append(output[-1] if output else 0)
            
            output.extend(match)
    
    return bytes(output)