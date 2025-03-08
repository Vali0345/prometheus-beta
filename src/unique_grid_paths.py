def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Handle edge cases
    if n < 2:
        return False
    
    # Check for divisibility up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_path(grid):
    """
    Find a continuous path of cells forming a prime number sequence.
    
    Args:
        grid (List[List[int]]): A 2D grid of integers.
    
    Returns:
        List[tuple]: A list of (row, col) coordinates forming a prime path, 
                     or an empty list if no prime path exists.
    """
    # Handle edge cases
    if not grid or not grid[0]:
        return []
    
    # Handle single cell case
    if len(grid) == 1 and len(grid[0]) == 1:
        return [(0, 0)] if is_prime(grid[0][0]) else []
    
    rows, cols = len(grid), len(grid[0])
    
    # Possible path directions with their respective steps
    path_directions = [
        # Horizontal, vertical, diagonals
        [(0, 1), (0, -1)],  # Horizontal
        [(1, 0), (-1, 0)],  # Vertical
        [(1, 1), (-1, -1)],  # Diagonal
        [(1, -1), (-1, 1)]  # Reverse diagonal
    ]
    
    def check_path(start_r, start_c, direction_set):
        """
        Check if a path forms a prime number.
        
        Args:
            start_r (int): Starting row
            start_c (int): Starting column
            direction_set (list): List of direction tuples
        
        Returns:
            List[tuple]: Prime path if found, else empty list
        """
        path = []
        current_r, current_c = start_r, start_c
        
        # Try both directions
        for step_r, step_c in direction_set:
            # Reset path and position for each direction
            path = [(current_r, current_c)]
            temp_r, temp_c = current_r, current_c
            
            # Try extending the path
            for _ in range(rows * cols):
                # Take a step in the direction
                temp_r += step_r
                temp_c += step_c
                
                # Check if new position is within grid
                if (0 <= temp_r < rows and 0 <= temp_c < cols):
                    path.append((temp_r, temp_c))
                    
                    # Check if path forms a prime number
                    sequence = [grid[r][c] for r, c in path]
                    number = int(''.join(map(str, sequence)))
                    
                    # Multi-digit prime with length > 1 is a valid solution
                    if is_prime(number) and len(path) > 1:
                        return path
                else:
                    break
        
        return []
    
    # Exhaustive search through all possible starting points
    for r in range(rows):
        for c in range(cols):
            for direction_set in path_directions:
                path = check_path(r, c, direction_set)
                if path:
                    return path
    
    # If no multi-digit prime path, return empty list
    return []