import random
from typing import List, TypeVar

T = TypeVar('T')

def shuffle_array(arr: List[T]) -> List[T]:
    """
    Shuffle the elements of an input array randomly.
    
    This function creates a new shuffled list, preserving the original array.
    Uses the Fisher-Yates (Knuth) shuffle algorithm for uniform randomness.
    
    Args:
        arr (List[T]): The input list to be shuffled
    
    Returns:
        List[T]: A new list with elements randomly shuffled
    
    Raises:
        TypeError: If input is not a list
    
    Examples:
        >>> shuffle_array([1, 2, 3, 4, 5])  # Returns a randomized version of the list
        >>> shuffle_array([])  # Returns an empty list
    """
    # Check for invalid input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the list to avoid modifying the original
    shuffled = arr.copy()
    
    # Fisher-Yates shuffle algorithm
    for i in range(len(shuffled) - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = random.randint(0, i)
        
        # Swap elements
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    
    return shuffled