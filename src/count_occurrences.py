def count_occurrences(arr, target):
    """
    Count the number of times a specific element appears in an array.

    Args:
        arr (list): The input array to search through.
        target: The element to count occurrences of.

    Returns:
        int: The number of times the target element appears in the array.

    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use list count method to find occurrences
    return arr.count(target)