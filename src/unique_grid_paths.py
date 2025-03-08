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
    
    # Directions for traversal
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0)   # Up
    ]
    
    def find_prime_path_from(start_r, start_c):
        """
        Find a prime path starting from a specific cell.
        
        Args:
            start_r (int): Starting row
            start_c (int): Starting column
        
        Returns:
            List[tuple]: Path of coordinates forming a prime sequence
        """
        for depth in range(1, rows * cols + 1):
            for initial_dir in directions:
                path = []
                current_r, current_c = start_r, start_c
                current_dir = initial_dir
                
                for _ in range(depth):
                    path.append((current_r, current_c))
                    
                    # Compute number sequence
                    sequence = [grid[r][c] for r, c in path]
                    number = int(''.join(map(str, sequence)))
                    
                    # Check primality conditions
                    if is_prime(number) and len(path) > 1:
                        return path
                    
                    # Attempt next step
                    next_r = current_r + current_dir[0]
                    next_c = current_c + current_dir[1]
                    
                    # Check grid bounds
                    if (0 <= next_r < rows and 0 <= next_c < cols):
                        current_r, current_c = next_r, next_c
                    else:
                        break
        
        return []
    
    # Search for the first valid prime path
    for r in range(rows):
        for c in range(cols):
            path = find_prime_path_from(r, c)
            if path:
                return path
    
    return []