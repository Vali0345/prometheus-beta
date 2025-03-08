import pytest
import math
from src.closest_points import find_closest_point_pairs

def test_basic_closest_points():
    """Test finding closest points with simple input"""
    list_a = [(0, 0), (1, 1), (3, 4)]
    list_b = [(2, 2), (5, 5), (0, 1)]
    
    result = find_closest_point_pairs(list_a, list_b)
    assert result is not None
    
    (point_a, point_b), distance = result
    
    # Expected point to minimize Euclidean distance
    expected_point_a = (0, 0)
    expected_point_b = (0, 1)
    expected_distance = math.sqrt((0 - 0)**2 + (0 - 1)**2)
    
    assert point_a == expected_point_a
    assert point_b == expected_point_b
    assert math.isclose(distance, expected_distance, rel_tol=1e-9)

def test_empty_lists():
    """Test behavior with empty lists"""
    assert find_closest_point_pairs([], []) is None
    assert find_closest_point_pairs([(0, 0)], []) is None
    assert find_closest_point_pairs([], [(0, 0)]) is None

def test_single_point_lists():
    """Test lists with single points"""
    list_a = [(1, 1)]
    list_b = [(2, 2)]
    
    result = find_closest_point_pairs(list_a, list_b)
    assert result is not None
    
    (point_a, point_b), distance = result
    
    assert point_a == (1, 1)
    assert point_b == (2, 2)
    assert math.isclose(distance, math.sqrt(2), rel_tol=1e-9)

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_closest_point_pairs("not a list", [(0, 0)])
    
    with pytest.raises(ValueError):
        find_closest_point_pairs([(0, 0)], [(1,)])
    
    with pytest.raises(ValueError):
        find_closest_point_pairs([(0, 0)], [("a", "b")])

def test_float_coordinates():
    """Test with floating point coordinates"""
    list_a = [(0.5, 1.2), (2.3, 4.5)]
    list_b = [(0.7, 1.3), (3.1, 4.8)]
    
    result = find_closest_point_pairs(list_a, list_b)
    assert result is not None
    
    (point_a, point_b), distance = result
    
    # Verify the pair with minimum Euclidean distance
    expected_point_a = (0.5, 1.2)
    expected_point_b = (0.7, 1.3)
    expected_distance = math.sqrt((0.5 - 0.7)**2 + (1.2 - 1.3)**2)
    
    assert point_a == expected_point_a
    assert point_b == expected_point_b
    assert math.isclose(distance, expected_distance, rel_tol=1e-9)