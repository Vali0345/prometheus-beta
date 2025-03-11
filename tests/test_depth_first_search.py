import pytest
from src.depth_first_search import depth_first_search

def test_basic_dfs():
    """Test basic DFS traversal."""
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    result = depth_first_search(graph, 'A')
    expected = ['A', 'B', 'D', 'E', 'F', 'C']
    assert result == expected

def test_dfs_with_visit_function():
    """Test DFS with a visit function."""
    visited_nodes = []
    def visit_fn(node):
        visited_nodes.append(node)
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }
    
    depth_first_search(graph, 'A', visit_fn)
    expected = ['A', 'B', 'D', 'C', 'E']
    assert visited_nodes == expected

def test_dfs_single_node_graph():
    """Test DFS on a graph with a single node."""
    graph = {'A': []}
    result = depth_first_search(graph, 'A')
    assert result == ['A']

def test_dfs_invalid_start_node():
    """Test DFS with a start node not in the graph."""
    graph = {'A': ['B'], 'B': []}
    
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        depth_first_search(graph, 'X')

def test_dfs_invalid_graph():
    """Test DFS with an invalid graph type."""
    with pytest.raises(TypeError, match="Graph must be a dictionary"):
        depth_first_search([], 'A')

def test_dfs_invalid_visit_function():
    """Test DFS with an invalid visit function."""
    graph = {'A': ['B'], 'B': []}
    
    with pytest.raises(TypeError, match="Visit function must be callable"):
        depth_first_search(graph, 'A', "not a function")

def test_dfs_disconnected_graph():
    """Test DFS on a disconnected graph."""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    
    result = depth_first_search(graph, 'A')
    assert set(result) == {'A', 'B'}