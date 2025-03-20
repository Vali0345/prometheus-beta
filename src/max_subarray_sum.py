def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray with length k in the given array.

    Args:
        arr (list): A list of integers to search for the maximum subarray sum.
        k (int): The length of the subarray.

    Returns:
        int: The maximum sum of any contiguous subarray of length k.
        If the array is empty or k is greater than array length, returns None.

    Raises:
        ValueError: If k is less than or equal to 0.

    Time Complexity: O(n), where n is the length of the array
    Space Complexity: O(1)
    """
    # Validate inputs
    if k <= 0:
        raise ValueError("Subarray length k must be a positive integer")
    
    # Handle edge cases
    if not arr or k > len(arr):
        return None
    
    # Initial window sum
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Sliding window approach
    for i in range(k, len(arr)):
        # Remove first element of previous window and add next element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum