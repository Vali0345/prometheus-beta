def is_digit_string(s: str) -> bool:
    """
    Check if a given string contains only digits.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string contains only digits, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> is_digit_string("12345")
        True
        >>> is_digit_string("123.45")
        False
        >>> is_digit_string("")
        False
        >>> is_digit_string("abc")
        False
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Check if the string is empty
    if not s:
        return False
    
    # Use string method to check if all characters are digits
    return s.isdigit()