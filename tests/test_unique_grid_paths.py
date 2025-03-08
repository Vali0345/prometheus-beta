import pytest
from src.unique_grid_paths import find_prime_path, is_prime

def test_is_prime():
    """Test prime number detection."""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(4) == False
    assert is_prime(15) == False

def test_find_prime_path_simple():
    """Test finding a prime path in a simple grid."""
    grid = [
        [1, 3, 7],
        [2, 5, 8],
        [9, 4, 6]
    ]
    path = find_prime_path(grid)
    assert path is not None
    assert len(path) > 0
    
    # Verify the path forms a prime number
    sequence = [grid[r][c] for r, c in path]
    number = int(''.join(map(str, sequence)))
    assert is_prime(number)

def test_find_prime_path_no_solution():
    """Test grid with no prime path."""
    grid = [
        [4, 6, 8],
        [9, 2, 5],
        [1, 3, 7]
    ]
    path = find_prime_path(grid)
    assert path == []

def test_find_prime_path_multiple_directions():
    """Test finding prime path with multiple direction changes."""
    grid = [
        [2, 3, 1],
        [5, 7, 9],
        [4, 6, 8]
    ]
    path = find_prime_path(grid)
    assert path is not None
    assert len(path) > 1
    
    # Verify the path forms a prime number
    sequence = [grid[r][c] for r, c in path]
    number = int(''.join(map(str, sequence)))
    assert is_prime(number)

def test_find_prime_path_edge_cases():
    """Test edge cases for grid traversal."""
    # Empty grid
    assert find_prime_path([]) == []
    
    # Single cell grid
    assert find_prime_path([[2]]) == [(0, 0)]
    assert find_prime_path([[4]]) == []

def test_prime_path_unique_starting_point():
    """Ensure the first valid prime path is returned."""
    grid = [
        [1, 7, 3],
        [2, 5, 8],
        [9, 4, 6]
    ]
    first_path = find_prime_path(grid)
    assert first_path is not None
    assert len(first_path) > 0
    
    # Verify primality
    sequence = [grid[r][c] for r, c in first_path]
    number = int(''.join(map(str, sequence)))
    assert is_prime(number)

def test_prime_path_bounded_movement():
    """Test that the path respects grid boundaries."""
    grid = [
        [2, 3, 1],
        [5, 7, 9],
        [4, 6, 8]
    ]
    path = find_prime_path(grid)
    
    # Check all path coordinates are within grid
    for r, c in path:
        assert 0 <= r < len(grid)
        assert 0 <= c < len(grid[0])