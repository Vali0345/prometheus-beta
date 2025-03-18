def min_reconstruction_operations(original, current):
    """
    Determine the minimum number of insertions and removals required to 
    transform the current sequence into the original sequence.
    
    Args:
        original (list): The target sequence to reconstruct
        current (list): The current sequence to transform
    
    Returns:
        int: Minimum number of operations (insertions/removals) needed
    
    Raises:
        ValueError: If input arguments are not valid lists
    """
    # Input validation
    if not isinstance(original, list) or not isinstance(current, list):
        raise ValueError("Both arguments must be lists")
    
    # Create frequency dictionaries to track element counts
    original_freq = {}
    current_freq = {}
    
    # Count frequencies in original sequence
    for item in original:
        original_freq[item] = original_freq.get(item, 0) + 1
    
    # Count frequencies in current sequence
    for item in current:
        current_freq[item] = current_freq.get(item, 0) + 1
    
    # Calculate operations needed
    total_operations = 0
    
    # Handle elements that need to be added or removed
    for item in set(list(original_freq.keys()) + list(current_freq.keys())):
        orig_count = original_freq.get(item, 0)
        curr_count = current_freq.get(item, 0)
        
        # Add operations needed to adjust this element's count
        total_operations += abs(orig_count - curr_count)
    
    return total_operations