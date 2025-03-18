def find_list_difference(list1, list2):
    """
    Find the difference between two lists.
    
    This function returns three sets:
    1. Elements unique to list1
    2. Elements unique to list2
    3. Elements common to both lists
    
    Args:
        list1 (list): The first input list
        list2 (list): The second input list
    
    Returns:
        tuple: A tuple containing three sets 
            (unique_to_list1, unique_to_list2, common_elements)
    
    Examples:
        >>> find_list_difference([1, 2, 3], [3, 4, 5])
        ({1, 2}, {4, 5}, {3})
        >>> find_list_difference([], [1, 2])
        (set(), {1, 2}, set())
    """
    # Convert lists to sets for efficient difference operations
    set1 = set(list1)
    set2 = set(list2)
    
    # Find elements unique to each list and common elements
    unique_to_list1 = set1 - set2
    unique_to_list2 = set2 - set1
    common_elements = set1 & set2
    
    return unique_to_list1, unique_to_list2, common_elements