def remove_duplicate_chars(input_string):
    """
    Remove duplicate characters from a given string, preserving the original order
    and ensuring that all characters in the same group (like words) are preserved.

    Args:
        input_string (str): The input string to remove duplicates from.

    Returns:
        str: A string with duplicate characters removed, keeping the first occurrence.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check for invalid input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # Use a dictionary to track seen characters in each word/group
    seen_chars = {}
    result = []

    # Split the input string into characters
    chars = list(input_string)

    for char in chars:
        # For each new word or group, reset the seen characters
        if char.isspace() and (not result or result[-1].isspace()):
            result.append(char)
        elif char not in seen_chars:
            result.append(char)
            seen_chars[char] = True

    return ''.join(result)