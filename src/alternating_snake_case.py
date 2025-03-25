def to_alternating_snake_case(input_string: str) -> str:
    """
    Convert a string to alternating snake case.
    
    Alternating snake case means:
    - Words are separated by underscores
    - Even-indexed words (0-based) are lowercase
    - Odd-indexed words are uppercase
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to alternating snake case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_alternating_snake_case("hello world")
        'hello_WORLD'
        >>> to_alternating_snake_case("python programming language")
        'python_PROGRAMMING_language'
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Split the input string into words
    words = input_string.split()
    
    # Convert words to alternating case
    converted_words = [
        word.lower() if idx % 2 == 0 else word.upper() 
        for idx, word in enumerate(words)
    ]
    
    # Join words with underscores
    return '_'.join(converted_words)