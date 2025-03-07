import pytest
from src.hopcroft_karp import HopcroftKarp

def test_simple_matching():
    """Test a simple bipartite graph with a clear maximum matching."""
    graph = {
        1: [4, 5],
        2: [4],
        3: [5]
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    
    # Validate matching
    assert len(matching) == 2  # Two nodes matched
    assert set(matching.values()) == {4, 5}  # Matched to 4 and 5
    assert set(matching.keys()).issubset({1, 2, 3})  # Matched from left nodes

def test_complete_graph():
    """Test a complete bipartite graph where every node can be matched."""
    graph = {
        1: [4, 5, 6],
        2: [4, 5, 6],
        3: [4, 5, 6]
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    
    # Validate matching
    assert len(matching) == 3  # All nodes matched
    # Each left node matched to a unique right node
    assert len(set(matching.values())) == 3

def test_no_matching():
    """Test a graph with no possible matching."""
    graph = {
        1: [],
        2: [],
        3: []
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    
    # Validate matching
    assert len(matching) == 0  # No nodes matched

def test_partial_matching():
    """Test a graph with partial matching possible."""
    graph = {
        1: [4],
        2: [5],
        3: [6],
        4: [7]
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    
    # Validate matching
    assert len(matching) >= 1  # At least one node matched
    assert len(matching) <= 2  # Maximum two nodes matched

def test_invalid_input():
    """Test error handling for invalid graph input."""
    with pytest.raises(TypeError):
        HopcroftKarp([1, 2, 3])  # Not a dictionary
    
    with pytest.raises(TypeError):
        HopcroftKarp("not a graph")  # Not a dictionary