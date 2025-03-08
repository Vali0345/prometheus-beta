import pytest
from src.color_stack_sorter import ColorStackSorter

def test_initial_validation():
    """Test that stacks must have equal length"""
    with pytest.raises(ValueError):
        ColorStackSorter(['red'], ['blue', 'green'], ['blue'])

def test_basic_sorting():
    """Test sorting a simple mixed stack configuration"""
    sorter = ColorStackSorter(
        ['blue', 'red', 'green'], 
        ['green', 'blue', 'red'], 
        ['red', 'green', 'blue']
    )
    moves = sorter.sort_stacks()
    
    # Verify sorting
    assert sorter.is_sorted() == True
    
    # Verify moves were made
    assert len(moves) > 0

def test_already_sorted():
    """Test scenario where stacks are already sorted"""
    sorter = ColorStackSorter(
        ['red', 'red', 'red'], 
        ['blue', 'blue', 'blue'], 
        ['green', 'green', 'green']
    )
    moves = sorter.sort_stacks()
    
    # Verify no moves made
    assert len(moves) == 0
    assert sorter.is_sorted() == True

def test_move_ball():
    """Test individual ball movement"""
    sorter = ColorStackSorter(
        ['blue'], 
        ['red'], 
        ['green']
    )
    
    # Move a ball
    sorter.move_ball('blue', 'red')
    
    # Check move was recorded
    assert len(sorter.moves) == 1
    assert sorter.moves[0] == ('blue', 'red')

def test_invalid_move():
    """Test moving from an empty stack"""
    sorter = ColorStackSorter(
        [], 
        ['red'], 
        ['green']
    )
    
    with pytest.raises(ValueError):
        sorter.move_ball('red', 'blue')

def test_complex_sorting():
    """Test a more complex mixing of balls"""
    sorter = ColorStackSorter(
        ['blue', 'red', 'green', 'blue'], 
        ['green', 'blue', 'red', 'red'], 
        ['red', 'green', 'blue', 'green']
    )
    moves = sorter.sort_stacks()
    
    # Verify sorting
    assert sorter.is_sorted() == True
    
    # Verify reasonable number of moves
    assert len(moves) > 0 and len(moves) < 100  # sanity check on moves

def test_edge_case_empty_stacks():
    """Test sorting with empty stacks"""
    sorter = ColorStackSorter([], [], [])
    moves = sorter.sort_stacks()
    
    # Verify sorting
    assert sorter.is_sorted() == True
    assert len(moves) == 0