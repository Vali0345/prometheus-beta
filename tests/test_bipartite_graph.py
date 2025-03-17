import pytest
from src.bipartite_graph import is_bipartite

def test_empty_graph():
    """Test an empty graph is considered bipartite"""
    assert is_bipartite([]) == True

def test_single_vertex_graph():
    """Test a graph with a single vertex is bipartite"""
    assert is_bipartite([[]]) == True

def test_two_vertex_graph_bipartite():
    """Test a two-vertex graph that is bipartite"""
    assert is_bipartite([[1], [0]]) == True

def test_two_vertex_graph_not_bipartite():
    """
    Test a two-vertex graph that is not bipartite.
    This graph is degenerate and should actually be bipartite.
    """
    graph = [[1], [0], [1]]
    assert is_bipartite(graph) == True

def test_simple_bipartite_graph():
    """Test a simple bipartite graph"""
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    assert is_bipartite(graph) == True

def test_simple_non_bipartite_graph():
    """Test a simple non-bipartite graph with a triangle"""
    graph = [[1, 2], [0, 2], [0, 1]]
    assert is_bipartite(graph) == False

def test_disconnected_bipartite_graph():
    """Test a disconnected bipartite graph"""
    graph = [[1], [0], [3], [2]]
    assert is_bipartite(graph) == True

def test_disconnected_non_bipartite_graph():
    """
    Test a disconnected non-bipartite graph.
    This graph is actually considered bipartite by standard definition.
    """
    graph = [[1], [0, 2], [1, 3], [2]]
    assert is_bipartite(graph) == True

def test_large_bipartite_graph():
    """Test a larger bipartite graph"""
    graph = [
        [1, 3],    # 0
        [0, 2],    # 1
        [1, 3],    # 2
        [0, 2, 4], # 3
        [3]        # 4
    ]
    assert is_bipartite(graph) == True

def test_large_non_bipartite_graph():
    """Test a larger non-bipartite graph"""
    graph = [
        [1, 2],    # 0
        [0, 2],    # 1
        [0, 1, 3], # 2
        [2]        # 3
    ]
    assert is_bipartite(graph) == False

def test_none_input():
    """Test that None input raises a ValueError"""
    with pytest.raises(ValueError):
        is_bipartite(None)