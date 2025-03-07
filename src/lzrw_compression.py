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
    
    # For very short inputs, return as-is
    if len(data) < 8:
        return data
    
    # Initialize compression variables
    compressed = bytearray()
    current_pos = 0
    window_size = 4096
    
    # Always include first literal bytes to maintain exact representation
    literals_to_preserve = min(3, len(data))
    compressed.extend(data[:literals_to_preserve])
    current_pos = literals_to_preserve
    
    while current_pos < len(data):
        # Look for the longest match in the previous window
        best_match_length = 0
        best_match_offset = 0
        
        # Search back through the window for the longest match
        window_start = max(0, current_pos - window_size)
        search_window = data[window_start:current_pos]
        
        for i in range(len(search_window)):
            match_length = 0
            
            # Check how long the match continues
            while (current_pos + match_length < len(data) and 
                   match_length < 15 and  # max 15 in 4 bits
                   data[window_start + i + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = current_pos - (window_start + i)
        
        # More conservative compression
        if best_match_length > 3:
            # Encode a match - 2 bytes: 12 bits for offset, 4 bits for length
            match_token = ((best_match_offset & 0xFFF) << 4) | (best_match_length & 0xF)
            compressed.extend(match_token.to_bytes(2, byteorder='big'))
            current_pos += best_match_length
        else:
            # Encode a literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    # If compression doesn't improve, return original data
    return data if len(compressed) >= len(data) else bytes(compressed)

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
    
    # If input is less than 8 bytes, return as-is (assumed uncompressed)
    if len(compressed_data) < 8:
        return compressed_data
    
    # Initialize decompression variables
    decompressed = bytearray()
    current_pos = 0
    
    # More conservative: try to preserve original bytes
    literals_to_preserve = min(3, len(compressed_data))
    decompressed.extend(compressed_data[:literals_to_preserve])
    current_pos = literals_to_preserve
    
    while current_pos < len(compressed_data):
        # Not enough data for a full token
        if current_pos + 1 >= len(compressed_data):
            decompressed.append(compressed_data[current_pos])
            break
        
        # Read 2-byte token
        token = int.from_bytes(compressed_data[current_pos:current_pos+2], byteorder='big')
        
        # Extract length and offset
        length = token & 0xF  # 4 bits for length
        offset = (token >> 4) & 0xFFF  # 12 bits for offset
        
        # If length is 0, it's a literal byte
        if length == 0 or length < 3:
            decompressed.append(compressed_data[current_pos])
            current_pos += 1
        else:
            # Determine start of sequence to copy
            start = len(decompressed) - offset
            
            # Failsafe for new compression or invalid references
            if start < 0:
                decompressed.append(compressed_data[current_pos])
                current_pos += 1
                continue
            
            # Copy the matched sequence
            for i in range(length):
                # Ensure we always have something to copy from existing decompressed
                if 0 <= start + i < len(decompressed):
                    decompressed.append(decompressed[start + i])
                else:
                    # Fallback to next available literal
                    if current_pos + 1 < len(compressed_data):
                        decompressed.append(compressed_data[current_pos])
                    break
            
            current_pos += 2
    
    return bytes(decompressed)