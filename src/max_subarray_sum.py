def max_subarray_sum_with_constraints(A, k, s):
    """
    Find the maximum sum of a contiguous subarray with at least k elements 
    and sum greater than or equal to s.
    
    Args:
        A (list): Input array of integers
        k (int): Minimum number of elements in the subarray
        s (int): Minimum sum threshold
    
    Returns:
        int: Maximum sum of a subarray meeting the constraints, 
             or -1 if no such subarray exists
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Handle invalid inputs
    if not A or k <= 0 or k > len(A):
        return -1
    
    # Initialize variables for sliding window approach
    max_sum = -1
    current_sum = 0
    current_length = 0
    left = 0
    
    for right in range(len(A)):
        # Add current element to the window
        current_sum += A[right]
        current_length += 1
        
        # Shrink window from left while it's too long
        while current_length > len(A):
            current_sum -= A[left]
            current_length -= 1
            left += 1
        
        # Shrink window from left while sum is too high or length is too long
        while left < right and (current_sum >= s and current_length >= k):
            # Update max_sum if it's the first valid sum or larger
            max_sum = max(max_sum, current_sum)
            
            # Remove leftmost element
            current_sum -= A[left]
            current_length -= 1
            left += 1
        
        # Check if current window meets constraints
        if current_length >= k and current_sum >= s:
            max_sum = max(max_sum, current_sum)
    
    return max_sum