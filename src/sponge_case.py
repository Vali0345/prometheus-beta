def to_sponge_case(text: str) -> str:
    """
    Convert a string to alternating sponge case (SpOnGeCase).
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The input string converted to sponge case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_sponge_case("hello")
        'hElLo'
        >>> to_sponge_case("WORLD")
        'wOrLd'
        >>> to_sponge_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If the string is empty, return it as-is
    if not text:
        return text
    
    # Convert to sponge case
    return ''.join(
        char.upper() if i % 2 else char.lower() 
        for i, char in enumerate(text)
    )