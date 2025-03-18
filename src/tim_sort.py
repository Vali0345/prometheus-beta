def insertion_sort(arr, left=0, right=None):
    """
    Perform insertion sort on a subsection of the array.
    
    Args:
        arr (list): The input list to be partially sorted
        left (int, optional): Starting index of the subsection. Defaults to 0.
        right (int, optional): Ending index of the subsection. Defaults to None.
    
    Returns:
        list: Partially sorted list
    """
    if right is None:
        right = len(arr) - 1
    
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[left..i-1] that are greater than key 
        # to one position ahead of their current position
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

def merge(arr, left, mid, right):
    """
    Merge two sorted subarrays of arr.
    
    Args:
        arr (list): The input list to be merged
        left (int): Starting index of the first subarray
        mid (int): Ending index of the first subarray
        right (int): Ending index of the second subarray
    
    Returns:
        list: Merged sorted list
    """
    # Create temp subarrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    # Initial indexes of first and second subarrays
    i = 0  # Initial index of left subarray
    j = 0  # Initial index of right subarray
    k = left  # Initial index of merged subarray
    
    # Merge the temp arrays back into arr[left..right]
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements of left_arr[] if any
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    # Copy remaining elements of right_arr[] if any
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    return arr

def tim_sort(arr, min_run=32):
    """
    Implements Tim Sort algorithm.
    
    Args:
        arr (list): Input list to be sorted
        min_run (int, optional): Minimum size of a run. Defaults to 32.
    
    Returns:
        list: Sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Type and input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Determine the size of runs
    n = len(arr)
    
    # Sort individual subarrays of size min_run
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)
    
    # Start merging from size min_run (or 32)
    size = min_run
    while size < n:
        # Pick starting point of different subarrays
        for start in range(0, n, size * 2):
            # Compute the midpoint and endpoint of subarrays
            mid = start + size - 1
            end = min(start + size * 2 - 1, n - 1)
            
            # Merge subarrays if mid is less than end
            if mid < end:
                merge(arr, start, mid, end)
        
        # Double the size of subarrays to be merged
        size *= 2
    
    return arr