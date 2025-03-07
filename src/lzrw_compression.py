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
    window_size = 4096  # Typical sliding window size
    max_match_length = 15  # Maximum match length in 4 bits
    
    # Initialize dictionary and pointers
    dictionary = {}
    current_pos = 0
    
    while current_pos < len(data):
        # Look for the longest match in the dictionary
        best_match_length = 0
        best_match_offset = 0
        
        # Search back through the window for the longest match
        search_start = max(0, current_pos - window_size)
        for offset in range(current_pos - search_start):
            match_length = 0
            while (current_pos + match_length < len(data) and 
                   match_length < max_match_length and
                   data[current_pos - offset + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = offset
        
        # Encode the match or literal
        if best_match_length > 2:
            # Encode match: (offset, length)
            # Use 12 bits for offset, 4 bits for length
            match_token = ((best_match_offset & 0xFFF) << 4) | (best_match_length & 0xF)
            compressed.extend(match_token.to_bytes(2, byteorder='big'))
            current_pos += best_match_length
        else:
            # Encode literal byte
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
        # Check if there's enough data to read a token
        if current_pos + 1 >= len(compressed_data):
            # If only one byte left, treat as literal
            decompressed.append(compressed_data[current_pos])
            break
        
        # Read the 2-byte token
        token = int.from_bytes(compressed_data[current_pos:current_pos+2], byteorder='big')
        
        # Extract offset and length
        offset = (token >> 4) & 0xFFF
        length = token & 0xF
        
        # If length is 0, it's a literal byte
        if length == 0:
            decompressed.append(compressed_data[current_pos])
            current_pos += 1
        else:
            # Copy matched sequence
            start = len(decompressed) - offset
            for i in range(length):
                if start + i < 0:
                    raise ValueError("Invalid compressed data: negative reference")
                decompressed.append(decompressed[start + i])
            
            current_pos += 2
    
    return bytes(decompressed)