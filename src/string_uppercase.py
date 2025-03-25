def convert_to_uppercase_with_spaces(input_string: str) -> str:
    """
    Convert a string to uppercase, preserving existing spaces and adding spaces between words.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The input string converted to uppercase with added spaces.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove multiple spaces and strip leading/trailing whitespace
    cleaned_string = ' '.join(input_string.split())
    
    # Convert to uppercase
    return cleaned_string.upper()