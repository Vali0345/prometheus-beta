import random
from typing import List, TypeVar

T = TypeVar('T')

def bogosort(arr: List[T]) -> List[T]:
    """
    Implement the bogosort (permutation sort) algorithm.
    
    Bogosort works by randomly shuffling the list until it becomes sorted.
    This is an extremely inefficient sorting algorithm with O(∞) time complexity.
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A sorted version of the input list
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains elements that cannot be compared
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Check if elements are comparable
    try:
        # Try to compare first two elements to ensure comparability
        if len(arr) > 1:
            _ = arr[0] < arr[1]
    except TypeError:
        raise ValueError("List elements must be comparable")
    
    # Create a copy to avoid modifying the original list
    working_list = arr.copy()
    
    # Shuffle and check if sorted
    while not is_sorted(working_list):
        random.shuffle(working_list)
    
    return working_list

def is_sorted(arr: List[T]) -> bool:
    """
    Check if a list is sorted in ascending order.
    
    Args:
        arr (List[T]): The list to check for sortedness
    
    Returns:
        bool: True if the list is sorted, False otherwise
    """
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))