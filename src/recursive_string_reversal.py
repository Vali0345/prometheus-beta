def recursive_reverse_string(s: str) -> str:
    """
    Recursively reverse a given string.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> recursive_reverse_string("hello")
        'olleh'
        >>> recursive_reverse_string("")
        ''
        >>> recursive_reverse_string("a")
        'a'
    """
    # Check for invalid input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    
    # Recursive case: first character moved to end of reversed substring
    return recursive_reverse_string(s[1:]) + s[0]