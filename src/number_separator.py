from typing import List, Tuple

def separate_evens_odds(numbers: List[int]) -> Tuple[List[int], List[int]]:
    """
    Separate a list of integers into even and odd numbers.

    Args:
        numbers (List[int]): A list of integers to be separated.

    Returns:
        Tuple[List[int], List[int]]: A tuple containing two lists:
            - First list: even numbers
            - Second list: odd numbers

    Raises:
        TypeError: If the input is not a list of integers.
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Separate even and odd numbers
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    
    return (evens, odds)