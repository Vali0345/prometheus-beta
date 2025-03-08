import math
from typing import List, Tuple, Optional

def find_closest_point_pairs(list_a: List[Tuple[float, float]], 
                              list_b: List[Tuple[float, float]]) -> Optional[Tuple[Tuple[Tuple[float, float], Tuple[float, float]], float]]:
    """
    Find the two closest points, one from list A and one from list B.
    
    Args:
        list_a (List[Tuple[float, float]]): First list of points (x, y coordinates)
        list_b (List[Tuple[float, float]]): Second list of points (x, y coordinates)
    
    Returns:
        Optional[Tuple[Tuple[Tuple[float, float], Tuple[float, float]], float]]: 
        A tuple containing:
        - A tuple of two points (one from list A, one from list B)
        - The Euclidean distance between these points
        Returns None if either input list is empty
    
    Raises:
        TypeError: If inputs are not lists of points
        ValueError: If points are not 2D coordinates
    """
    # Validate input
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise TypeError("Inputs must be lists of points")
    
    # Check for empty lists
    if not list_a or not list_b:
        return None
    
    # Validate point format
    def validate_point(point, list_name):
        if not isinstance(point, tuple) or len(point) != 2 or \
           not all(isinstance(coord, (int, float)) for coord in point):
            raise ValueError(f"Invalid point in {list_name}: {point}")
    
    for point in list_a:
        validate_point(point, "list A")
    for point in list_b:
        validate_point(point, "list B")
    
    # Find the closest pair
    min_distance = float('inf')
    closest_pair = None
    
    for point_a in list_a:
        for point_b in list_b:
            # Calculate Euclidean distance
            distance = math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)
            
            # Update minimum distance if current distance is smaller
            if distance < min_distance:
                min_distance = distance
                closest_pair = (point_a, point_b)
    
    return (closest_pair, min_distance)