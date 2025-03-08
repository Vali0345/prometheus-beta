def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within a given array of integers.
    
    This implementation uses Kadane's algorithm to efficiently find the maximum 
    subarray sum in O(n) time complexity.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is empty
    
    Examples:
        >>> max_subarray_sum([1, -2, 3, 4, -1, 5])
        11
        >>> max_subarray_sum([-1, -2, -3])
        -1
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Check for empty list
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_ending_here = max_so_far = arr[0]
    
    # Iterate through the array using Kadane's algorithm
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new subarray
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum sum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far