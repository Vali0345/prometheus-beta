def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Find the median of two sorted arrays in O(log(min(m,n))) time complexity.
    
    Args:
        nums1 (list[int]): First sorted input array
        nums2 (list[int]): Second sorted input array
    
    Returns:
        float: Median of the two sorted arrays
    
    Raises:
        TypeError: If inputs are not lists
        ValueError: If inputs contain non-numeric elements
    
    Examples:
        >>> find_median_sorted_arrays([1,3], [2])
        2.0
        >>> find_median_sorted_arrays([1,2], [3,4])
        2.5
    """
    # Validate input types
    if not (isinstance(nums1, list) and isinstance(nums2, list)):
        raise TypeError("Inputs must be lists")
    
    # Validate input contains only numbers
    if not (all(isinstance(x, (int, float)) for x in nums1) and 
            all(isinstance(x, (int, float)) for x in nums2)):
        raise ValueError("Lists must contain only numeric values")
    
    # Ensure nums1 is the smaller array for optimization
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        partition_x = (left + right) // 2
        partition_y = (m + n + 1) // 2 - partition_x
        
        # Find max and min values at partition points
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == m else nums1[partition_x]
        
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == n else nums2[partition_y]
        
        # Check if we have found the correct partition
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            # If total length is even
            if (m + n) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            # If total length is odd
            else:
                return max(max_left_x, max_left_y)
        
        # Adjust partitions
        elif max_left_x > min_right_y:
            right = partition_x - 1
        else:
            left = partition_x + 1
    
    # If no valid partition found
    raise ValueError("Input arrays must be sorted")