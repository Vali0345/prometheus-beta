"""
Module for logging messages with indentation.
"""

def log_with_indent(message, indent_level=0, indent_char=' '):
    """
    Log a message with specified indentation.

    Args:
        message (str): The message to be logged.
        indent_level (int, optional): Number of indentation levels. Defaults to 0.
        indent_char (str, optional): Character used for indentation. Defaults to space.

    Returns:
        str: The indented message.

    Raises:
        TypeError: If message is not a string or indent_level is not an integer.
        ValueError: If indent_level is negative or indent_char is not a single character.
    """
    # Type checking
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not isinstance(indent_level, int):
        raise TypeError("Indent level must be an integer")
    
    if indent_level < 0:
        raise ValueError("Indent level cannot be negative")
    
    if not isinstance(indent_char, str) or len(indent_char) != 1:
        raise ValueError("Indent character must be a single character")
    
    # Create indentation
    indentation = indent_char * (indent_level * 4)
    
    # Apply indentation to each line of the message
    indented_lines = [f"{indentation}{line}" for line in message.splitlines()]
    
    # Join the lines back together
    return '\n'.join(indented_lines)