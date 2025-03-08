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
    
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    def dfs(row, col, current_path, visited):
        """
        Depth-first search to find prime paths.
        
        Args:
            row (int): Current row
            col (int): Current column
            current_path (List[tuple]): Current path of coordinates
            visited (set): Set of visited coordinates
        
        Returns:
            List[tuple]: A valid prime path if found, else empty list
        """
        # If path is too long, backtrack
        if len(current_path) > rows * cols:
            return []
        
        # Check current path
        if len(current_path) > 1:
            sequence = [grid[r][c] for r, c in current_path]
            number = int(''.join(map(str, sequence)))
            if is_prime(number):
                return current_path
        
        # Try all four directions
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Check bounds and avoid revisiting
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited):
                
                # Create new path and visited set
                new_path = current_path + [(new_row, new_col)]
                new_visited = visited.copy()
                new_visited.add((new_row, new_col))
                
                # Recursively search
                result = dfs(new_row, new_col, new_path, new_visited)
                if result:
                    return result
        
        return []
    
    # Special case: check if grid has a prime solution by exhaustive search
    for length in range(1, rows * cols + 1):
        # Iterate through every starting position
        for start_r in range(rows):
            for start_c in range(cols):
                for r_step in range(-1, 2):
                    for c_step in range(-1, 2):
                        # Skip invalid or zero-movement directions
                        if r_step == 0 and c_step == 0:
                            continue
                        
                        # Try to build a path
                        path = []
                        current_r, current_c = start_r, start_c
                        
                        for _ in range(length):
                            # Check grid bounds
                            if (0 <= current_r < rows and 
                                0 <= current_c < cols):
                                path.append((current_r, current_c))
                                current_r += r_step
                                current_c += c_step
                            else:
                                break
                        
                        # If path has enough length, verify prime sequence
                        if len(path) >= length:
                            sequence = [grid[r][c] for r, c in path]
                            number = int(''.join(map(str, sequence)))
                            if is_prime(number):
                                return path
    
    return []