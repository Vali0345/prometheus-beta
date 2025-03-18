def compute_lps(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array.
    
    This is a helper function for the KMP algorithm that precomputes 
    the prefix-suffix matches to optimize string searching.
    
    Args:
        pattern (str): The pattern string to compute LPS for
    
    Returns:
        list: An array of LPS values for each index in the pattern
    """
    # Handle empty string case
    if not pattern:
        return []
    
    # Length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    length = 0  # Length of the current longest prefix suffix
    i = 1
    
    # Compute LPS array
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            # If characters match, extend the prefix
            length += 1
            lps[i] = length
            i += 1
        else:
            # If characters don't match
            if length != 0:
                # Go back to the previous longest prefix suffix
                length = lps[length - 1]
            else:
                # No prefix found
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform KMP (Knuth-Morris-Pratt) string matching algorithm.
    
    Finds all occurrences of a pattern within a text.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all occurrences of the pattern in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If pattern is an empty string unless text is also empty
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    # Special handling for empty pattern and empty text
    if not pattern:
        if not text:
            return []
        raise ValueError("Pattern cannot be an empty string")
    
    # If pattern is longer than text, no match is possible
    if len(pattern) > len(text):
        return []
    
    # Compute the LPS array for the pattern
    lps = compute_lps(pattern)
    
    # List to store all match indices
    matches = []
    
    # Pointers for text and pattern
    i = 0  # text index
    j = 0  # pattern index
    
    # Perform case-sensitive search (by keeping case the same)
    text = text
    pattern = pattern
    
    while i < len(text):
        # If characters match, move both pointers
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # Pattern fully matched
        if j == len(pattern):
            matches.append(i - j)
            # Reset j to the proper prefix
            j = lps[j - 1]
        
        # Mismatch after some matches
        elif i < len(text) and text[i] != pattern[j]:
            # If j is not at the start, use LPS to skip characters
            if j != 0:
                j = lps[j - 1]
            else:
                # If j is at the start, move text pointer
                i += 1
    
    return matches