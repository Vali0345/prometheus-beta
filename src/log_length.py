import logging

def log_length(input_obj):
    """
    Log the length of a string or array.

    Args:
        input_obj (str or list or tuple): The input to measure length of.

    Returns:
        int: The length of the input object.

    Raises:
        TypeError: If the input is not a string, list, or tuple.
    """
    # Validate input type
    if not isinstance(input_obj, (str, list, tuple)):
        raise TypeError("Input must be a string, list, or tuple")
    
    # Calculate length
    length = len(input_obj)
    
    # Log the length
    logging.info(f"Length of input: {length}")
    
    return length