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
    
    # Add termination character if not present
    modified_text = input_text + '$' if '$' not in input_text else input_text
    
    # Generate all rotations
    n = len(modified_text)
    rotations = [modified_text[i:] + modified_text[:i] for i in range(n)]
    
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
    
    # Count character frequencies in the BWT string
    char_freq = {}
    for char in bwt_string:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Create first column by sorting the last column (BWT)
    first_column = sorted(bwt_string)
    
    # Compute the next index for each character
    next_indices = {}
    char_counts = {}
    
    for i, char in enumerate(first_column):
        if char not in char_counts:
            char_counts[char] = 0
        
        # Find the correct occurrence of this character in the BWT string
        for j, bwt_char in enumerate(bwt_string):
            if bwt_char == char:
                if char_counts[char] == 0:
                    next_indices[i] = j
                    break
                char_counts[char] -= 1
    
    # Reconstruct the original string
    result = []
    current = original_index
    
    for _ in range(len(bwt_string)):
        # Append character from first column
        result.append(first_column[current])
        
        # Move to the next index
        current = next_indices[current]
    
    # Reconstruct and remove termination character
    reconstructed = ''.join(result)
    
    # Return the string without the termination character
    return reconstructed.split('$')[0]