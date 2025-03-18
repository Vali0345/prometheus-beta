def burrows_wheeler_transform(input_text):
    """
    Implement the Burrows-Wheeler Transform for data compression.
    
    The Burrows-Wheeler Transform (BWT) is a reversible transformation 
    used in data compression algorithms.
    
    Args:
        input_text (str): The input string to be transformed.
    
    Returns:
        tuple: A tuple containing:
            - The transformed string (last column of sorted rotations)
            - The index of the original string in the sorted rotations
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    """
    # Validate input
    if not isinstance(input_text, str):
        raise TypeError("Input must be a string")
    
    if not input_text:
        raise ValueError("Input string cannot be empty")
    
    # Add termination character
    modified_text = input_text + '$'
    
    # Generate all rotations
    rotations = [modified_text[i:] + modified_text[:i] for i in range(len(modified_text))]
    
    # Sort rotations lexicographically 
    sorted_rotations = sorted(rotations)
    
    # Get the last column of sorted rotations (Burrows-Wheeler Transform)
    bwt_string = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    # Find the index of the original string in sorted rotations
    original_index = sorted_rotations.index(modified_text)
    
    return bwt_string, original_index

def inverse_burrows_wheeler_transform(bwt_string, original_index):
    """
    Reverse the Burrows-Wheeler Transform to recover the original string.
    
    Args:
        bwt_string (str): The Burrows-Wheeler transformed string
        original_index (int): The index of the original string in sorted rotations
    
    Returns:
        str: The original input string
    
    Raises:
        TypeError: If inputs are of incorrect type
        ValueError: If inputs are invalid
    """
    # Validate inputs
    if not isinstance(bwt_string, str):
        raise TypeError("BWT string must be a string")
    
    if not isinstance(original_index, int):
        raise TypeError("Original index must be an integer")
    
    if not bwt_string:
        raise ValueError("BWT string cannot be empty")
    
    if original_index < 0 or original_index >= len(bwt_string):
        raise ValueError("Invalid original index")
    
    # Sort the BWT string to create the first column
    first_column = sorted(bwt_string)
    
    # Create a mapping to track occurrences
    last_to_first = {}
    first_occurrence = {}
    
    # First pass: track first occurrence of each character in first column
    for i, char in enumerate(first_column):
        if char not in first_occurrence:
            first_occurrence[char] = i
    
    # Second pass: create last to first mapping
    char_count = {}
    for j, char in enumerate(bwt_string):
        # Count occurrences of this character in last column
        count = char_count.get(char, 0)
        
        # Find the corresponding index in first column
        last_to_first[j] = first_occurrence[char] + count
        
        # Increment character count
        char_count[char] = count + 1
    
    # Reconstruct the original string
    result = []
    current = original_index
    
    for _ in range(len(bwt_string)):
        # Append the character from the first column
        result.append(first_column[current])
        
        # Move to the next index using last-to-first mapping
        current = last_to_first[current]
    
    # Convert back to original string (remove termination character)
    reconstructed = ''.join(result)
    return reconstructed.rstrip('$')