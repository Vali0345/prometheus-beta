def find_middle_range_indices(sorted_list, range_radius):
    """
    Find indices of elements within a given range of the middle value in a sorted list.

    Args:
        sorted_list (list): A sorted list of integers
        range_radius (int): The number of indices to include on each side of the middle

    Returns:
        list: Indices of elements within the specified range of the middle value

    Raises:
        ValueError: If the input list is empty
        TypeError: If inputs are not of the correct type
    """
    # Validate inputs
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(range_radius, int):
        raise TypeError("Range radius must be an integer")
    
    if len(sorted_list) == 0:
        raise ValueError("Input list cannot be empty")
    
    if range_radius < 0:
        raise ValueError("Range radius must be non-negative")
    
    # Calculate the middle index
    if len(sorted_list) % 2 == 0:
        # For even-length lists, take the lower middle index
        middle_index = len(sorted_list) // 2 - 1
    else:
        # For odd-length lists, take the exact middle index
        middle_index = len(sorted_list) // 2
    
    # Calculate the range of indices
    start_index = max(0, middle_index - range_radius)
    end_index = min(len(sorted_list) - 1, middle_index + range_radius)
    
    # Return the indices within the specified range
    return list(range(start_index, end_index + 1))