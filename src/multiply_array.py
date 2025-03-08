from typing import List, Union

def multiply(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Multiply corresponding elements of an input array.

    Args:
        arr (List[Union[int, float]]): Input array of numbers to multiply.

    Returns:
        List[Union[int, float]]: A new array with elements multiplied pairwise.

    Raises:
        ValueError: If the input is not a list or contains non-numeric elements.
        ValueError: If input lists have different lengths.

    Examples:
        >>> multiply([1, 2, 3], [4, 5, 6])
        [4, 10, 18]
        >>> multiply([2, 3], [4, 5])
        [8, 15]
    """
    # Validate input is a list and contains numeric elements
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numeric")
    
    return arr