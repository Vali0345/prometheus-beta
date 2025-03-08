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
    
    def find_prime_sequence(cells):
        """
        Check if a sequence of cells forms a multi-digit prime number.
        
        Args:
            cells (List[tuple]): List of (row, col) coordinates
        
        Returns:
            bool: Whether the sequence forms a multi-digit prime
        """
        if len(cells) <= 1:
            return False
        
        sequence = [grid[r][c] for r, c in cells]
        number = int(''.join(map(str, sequence)))
        
        return is_prime(number) and len(str(number)) > 1
    
    def dfs(row, col, path, visited):
        """
        Depth-first search to find prime paths.
        
        Args:
            row (int): Current row
            col (int): Current column
            path (List[tuple]): Current path of coordinates
            visited (set): Set of visited coordinates
        
        Returns:
            List[tuple]: Prime path if found, else empty list
        """
        # Limit path length
        if len(path) > rows * cols:
            return []
        
        # Check current path
        if find_prime_sequence(path):
            return path
        
        # Explore in different directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check grid bounds and avoid revisiting
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited):
                
                # Create new path and visited set
                new_path = path + [(new_row, new_col)]
                new_visited = visited.copy()
                new_visited.add((new_row, new_col))
                
                # Recursively search
                result = dfs(new_row, new_col, new_path, new_visited)
                if result:
                    return result
        
        return []
    
    # Try from every starting point
    for r in range(rows):
        for c in range(cols):
            result = dfs(r, c, [(r, c)], {(r, c)})
            if result:
                return result
    
    return []