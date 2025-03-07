"""
LZRW Compression Algorithm Implementation.

This module provides a basic implementation of the LZRW (Lempel-Ziv Ross Williams) 
compression algorithm, which is a simple and fast data compression technique.
"""

def compress(data):
    """
    Compress input data using the LZRW compression algorithm.
    
    Args:
        data (bytes or str): The input data to be compressed.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
    """
    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # If input is empty, return empty bytes
    if not data:
        return b''
    
    # Initialize compression variables
    compressed = bytearray()
    current_pos = 0
    
    while current_pos < len(data):
        # Look for the longest match in the previous window
        max_match_length = 0
        max_match_offset = 0
        
        # Search back through a maximum of 4096-byte window
        window_start = max(0, current_pos - 4096)
        window = data[window_start:current_pos]
        
        for i in range(len(window)):
            match_length = 0
            
            # Check how long the match continues
            while (current_pos + match_length < len(data) and 
                   data[window_start + i + match_length] == data[current_pos + match_length]):
                match_length += 1
                
                # Stop if match is too long (15 is max with 4 bits)
                if match_length == 15:
                    break
            
            # Update best match if found
            if match_length > max_match_length:
                max_match_length = match_length
                max_match_offset = current_pos - (window_start + i)
        
        # Encode the match or literal
        if max_match_length > 2:
            # Encode a match - 2 bytes: 12 bits for offset, 4 bits for length
            match_token = ((max_match_offset & 0xFFF) << 4) | (max_match_length & 0xF)
            compressed.extend(match_token.to_bytes(2, byteorder='big'))
            current_pos += max_match_length
        else:
            # Encode a literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    return bytes(compressed)

def decompress(compressed_data):
    """
    Decompress data previously compressed with LZRW algorithm.
    
    Args:
        compressed_data (bytes): The compressed data to be decompressed.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If compressed data is invalid.
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # If input is empty, return empty bytes
    if not compressed_data:
        return b''
    
    # Initialize decompression variables
    decompressed = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        # If only one byte left or first byte
        if current_pos + 1 >= len(compressed_data):
            # Treat as a literal byte
            decompressed.append(compressed_data[current_pos])
            break
        
        # Read 2-byte token
        token = int.from_bytes(compressed_data[current_pos:current_pos+2], byteorder='big')
        
        # Extract offset and length
        length = token & 0xF  # 4 bits for length
        offset = (token >> 4) & 0xFFF  # 12 bits for offset
        
        # If length is 0, it's a literal byte
        if length == 0:
            decompressed.append(compressed_data[current_pos])
            current_pos += 1
        else:
            # Copy matched sequence
            start = len(decompressed) - offset
            
            # Handle invalid references
            if start < 0:
                raise ValueError("Invalid compressed data: negative reference")
            
            # Copy the matched sequence
            for i in range(length):
                if start + i >= len(decompressed):
                    # If the reference exceeds current decompressed data, we may have a problem
                    raise ValueError("Invalid compressed data: reference out of bounds")
                
                decompressed.append(decompressed[start + i])
            
            current_pos += 2
    
    return bytes(decompressed)