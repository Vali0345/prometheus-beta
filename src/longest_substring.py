def find_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.
    
    This function is case-sensitive, meaning 'A' and 'a' are considered different characters.
    
    Args:
        s (str): The input string to search for the longest substring.
    
    Returns:
        str: The longest substring without repeating characters.
             If multiple such substrings exist with the same maximum length, 
             returns the first occurrence.
    
    Examples:
        >>> find_longest_substring("abcabcbb")
        'abc'
        >>> find_longest_substring("bbbbb")
        'b'
        >>> find_longest_substring("")
        ''
    """
    # Handle empty string case
    if not s:
        return ""
    
    # Sliding window approach
    start = 0
    max_length = 0
    max_substring = ""
    char_map = {}
    
    for end, char in enumerate(s):
        # If character is in map and its last position is after or equal to start
        if char in char_map and char_map[char] >= start:
            # Move start to the next position after last occurrence of repeated char
            start = char_map[char] + 1
        else:
            # Update max substring if current substring is longer
            if end - start + 1 > max_length:
                max_length = end - start + 1
                max_substring = s[start:end+1]
        
        # Update last seen position of character
        char_map[char] = end
    
    return max_substring