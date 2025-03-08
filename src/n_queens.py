def solve_n_queens(n):
    """
    Solve the N-Queens problem by finding all possible arrangements 
    of N queens on an NxN chessboard where no queens threaten each other.
    
    Args:
        n (int): Size of the chessboard and number of queens to place.
    
    Returns:
        list: A list of all valid queen arrangements, where each arrangement 
              is represented as a list of column positions for each row.
    
    Raises:
        ValueError: If n is less than 1.
    """
    # Validate input
    if n < 1:
        raise ValueError("Board size must be at least 1")
    
    def is_safe(board, row, col):
        """
        Check if a queen can be placed on board[row][col] without being threatened.
        
        Args:
            board (list): Current board configuration
            row (int): Row to place the queen
            col (int): Column to place the queen
        
        Returns:
            bool: True if the queen can be placed safely, False otherwise
        """
        # Check this row on the left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # Check upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal on the left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True
    
    def solve(board, col, solutions):
        """
        Recursive backtracking function to solve N-Queens problem.
        
        Args:
            board (list): Current board configuration
            col (int): Current column being processed
            solutions (list): List to store valid solutions
        """
        # Base case: if all queens are placed, add the solution
        if col >= n:
            # Extract column positions for each row
            solution = []
            for row in range(n):
                solution.append(board[row].index(1))
            solutions.append(solution)
            return
        
        # Consider this column and try placing queens in all rows
        for row in range(n):
            # Create a copy of the board to avoid modifying the original
            board_copy = [r.copy() for r in board]
            
            # If queen can be placed safely
            if is_safe(board_copy, row, col):
                # Place the queen
                board_copy[row][col] = 1
                
                # Recursively place queens in remaining columns
                solve(board_copy, col + 1, solutions)
    
    # Initialize empty board
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    
    # Find all solutions
    solve(board, 0, solutions)
    
    return solutions