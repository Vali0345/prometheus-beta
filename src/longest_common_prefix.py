def find_longest_common_prefix(strings):
    """
    Find the longest common prefix among a list of strings.

    Args:
        strings (list): A list of strings to find the common prefix for.

    Returns:
        str: The longest common prefix. Returns an empty string if no common prefix exists.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list contains non-string elements.
    """
    # Handle edge cases
    if not strings:
        return ""
    
    # Validate input type
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    # Validate list contains only strings
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    
    # If only one string, return that string
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string to limit prefix search
    shortest = min(strings, key=len)
    
    # Iterate through characters of the shortest string
    for i in range(len(shortest)):
        # Check if current character matches in all strings
        if any(string[i] != shortest[i] for string in strings):
            return shortest[:i]
    
    # If we've made it through the entire shortest string, return it
    return shortest