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
    longest_substring = ""
    current_substring = ""
    
    for char in s:
        # If character is already in current substring, 
        # trim the substring from the first occurrence of the repeated character
        if char in current_substring:
            # Keep track of the longest substring found so far
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            
            # Remove characters up to and including the first repeated character
            current_substring = current_substring[current_substring.index(char) + 1:] + char
        else:
            # Add character to current substring
            current_substring += char
    
    # Final check to see if the last substring is the longest
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring
    
    return longest_substring