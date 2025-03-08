import pytest
from src.n_queens import solve_n_queens

def test_n_queens_invalid_input():
    """Test that invalid input raises a ValueError"""
    with pytest.raises(ValueError):
        solve_n_queens(0)
    with pytest.raises(ValueError):
        solve_n_queens(-1)

def test_n_queens_1():
    """Test 1-queen problem"""
    solutions = solve_n_queens(1)
    assert len(solutions) == 1
    assert solutions[0] == [0]

def test_n_queens_4():
    """Test 4-queen problem"""
    solutions = solve_n_queens(4)
    
    # Expected unique solutions for 4-queens
    expected_solutions = [
        [1, 3, 0, 2],
        [2, 0, 3, 1]
    ]
    
    # Convert solutions to sorted list to handle order
    solution_set = set(tuple(sol) for sol in solutions)
    expected_set = set(tuple(sol) for sol in expected_solutions)
    
    assert solution_set == expected_set
    assert len(solutions) == 2

def test_n_queens_8():
    """Test 8-queen problem"""
    solutions = solve_n_queens(8)
    assert len(solutions) == 92  # Known number of solutions for 8-queens

def test_solution_validity():
    """Test that solutions meet N-Queens constraints"""
    for n in range(1, 6):  # Test for board sizes 1 to 5
        solutions = solve_n_queens(n)
        
        for solution in solutions:
            # Verify solution length matches board size
            assert len(solution) == n
            
            # Check no two queens share a row (redundant, but good for validation)
            assert len(set(solution)) == n
            
            # Check diagonal and anti-diagonal conflicts
            for i in range(n):
                for j in range(i+1, n):
                    # Check diagonal conflicts
                    assert abs(solution[i] - solution[j]) != abs(i - j)