def flatten_nested_list(nested_list):
    """
    Flatten a potentially deeply nested list into a single-level list.
    
    This function recursively flattens lists of any depth, handling 
    nested lists, tuples, and mixed iterables.
    
    Args:
        nested_list (list): A potentially nested list to be flattened
    
    Returns:
        list: A completely flattened list
    
    Raises:
        TypeError: If the input is not an iterable
    
    Examples:
        >>> flatten_nested_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_nested_list([])
        []
    """
    # Handle input validation
    if not hasattr(nested_list, '__iter__') or isinstance(nested_list, str):
        raise TypeError("Input must be an iterable (not a string)")
    
    # Initialize the flattened list
    flattened = []
    
    # Recursive flattening
    for item in nested_list:
        # If the item is an iterable (but not a string), recursively flatten
        if hasattr(item, '__iter__') and not isinstance(item, str):
            flattened.extend(flatten_nested_list(item))
        else:
            # If it's not an iterable, add the item directly
            flattened.append(item)
    
    return flattened