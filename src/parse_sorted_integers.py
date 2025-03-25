def parse_sorted_comma_integers(input_string):
    """
    Parse a string of comma-separated integers and return a sorted list.

    This function does the following:
    - Splits the input string by commas
    - Filters out non-integer characters
    - Converts valid integer strings to integers
    - Sorts the resulting list of integers

    Args:
        input_string (str): A string containing comma-separated integers.

    Returns:
        list: A sorted list of integers extracted from the input string.

    Examples:
        >>> parse_sorted_comma_integers("1,2,3")
        [1, 2, 3]
        >>> parse_sorted_comma_integers("10,2abc,3def")
        [2, 3, 10]
        >>> parse_sorted_comma_integers("")
        []
    """
    # Handle empty string case
    if not input_string:
        return []
    
    # Split by comma and process each part
    parsed_integers = []
    for part in input_string.split(','):
        # Remove non-digit characters
        cleaned_part = ''.join(char for char in part if char.isdigit())
        
        # Convert to integer if not empty
        if cleaned_part:
            try:
                parsed_integers.append(int(cleaned_part))
            except ValueError:
                # Skip if conversion fails (though this should not happen due to previous cleaning)
                continue
    
    # Return sorted list
    return sorted(parsed_integers)