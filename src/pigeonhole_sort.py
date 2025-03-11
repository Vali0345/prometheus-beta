def pigeonhole_sort(arr):
    """
    Implement the Pigeonhole Sort algorithm.
    
    Pigeonhole sort is an efficient sorting algorithm for lists with a known, 
    limited range of integer values. It works by distributing elements into 
    a set of "pigeonholes" and then collecting them back in order.
    
    Args:
        arr (list): A list of integers to be sorted
    
    Returns:
        list: A sorted version of the input list
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains non-integer elements
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(arr) <= 1:
        return arr.copy()
    
    # Validate input contains only integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Find the range of values
    min_val = min(arr)
    max_val = max(arr)
    
    # Create pigeonholes
    range_size = max_val - min_val + 1
    pigeonholes = [0] * range_size
    
    # Count occurrences of each value
    for num in arr:
        pigeonholes[num - min_val] += 1
    
    # Reconstruct the sorted array
    sorted_arr = []
    for i, count in enumerate(pigeonholes):
        sorted_arr.extend([i + min_val] * count)
    
    return sorted_arr