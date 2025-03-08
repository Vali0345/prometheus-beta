def find_pair_with_target(nums, target):
    """
    Find index pairs in a list of unique integers that sum up to the target.

    Args:
        nums (list): A list of unique integers.
        target (int): The target sum to find.

    Returns:
        list: A list of index pairs where the numbers at those indices sum to the target.
              Returns an empty list if no such pairs exist.

    Raises:
        TypeError: If input is not a list or target is not an integer.
        ValueError: If nums contains non-integer elements.
    """
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Ensure all elements are integers
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All elements in the list must be integers")
    
    # Use a dictionary to store complement values and their indices
    complement_dict = {}
    result = []
    
    # Iterate through the list with enumeration to keep track of indices
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in our dictionary
        if complement in complement_dict:
            # Add all pairs of indices where complement is found
            for j in complement_dict[complement]:
                # Ensure unique index pairs and avoid pairing an index with itself
                if j != i:
                    result.append([j, i])
        
        # Store the current number's index in the dictionary
        if num not in complement_dict:
            complement_dict[num] = []
        complement_dict[num].append(i)
    
    return result