def array_difference_mod(A, B):
    """
    Calculate element-wise difference between two arrays with modulo 10 and non-negative constraint.
    
    Args:
        A (list): First input array of integers (length 10)
        B (list): Second input array of integers (length 10)
    
    Returns:
        list: Array C where C[i] = max(0, (A[i] - B[i]) % 10)
    
    Raises:
        ValueError: If input arrays are not of length 10
    """
    # Validate input array lengths
    if len(A) != 10 or len(B) != 10:
        raise ValueError("Both input arrays must be of length 10")
    
    # Modify the comprehension to handle negative differences
    return [max(0, (a - b) % 10) for a, b in zip(A, B)]