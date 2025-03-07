def to_alternating_constant_case(input_string):
    """
    Convert a string to alternating constant case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to alternating constant case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_alternating_constant_case("hello")
        'HELLO'
        >>> to_alternating_constant_case("hello world")
        'HELLO WORLD'
        >>> to_alternating_constant_case("Python is awesome")
        'PYTHON IS AWESOME'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert the entire string to uppercase
    return input_string.upper()