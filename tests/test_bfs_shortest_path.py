import pytest
from src.bfs_shortest_path import find_shortest_path

def test_basic_path():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    assert find_shortest_path(graph, 'A', 'F') == ['A', 'C', 'F']

def test_same_node():
    graph = {
        'A': ['B', 'C'],
        'B': ['A'],
        'C': ['B']
    }
    assert find_shortest_path(graph, 'A', 'A') == ['A']

def test_direct_connection():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A'],
        'D': ['B']
    }
    assert find_shortest_path(graph, 'A', 'B') == ['A', 'B']

def test_no_path():
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    assert find_shortest_path(graph, 'A', 'C') is None

def test_numeric_nodes():
    graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6],
        4: [2],
        5: [2, 6],
        6: [3, 5]
    }
    assert find_shortest_path(graph, 1, 6) == [1, 3, 6]

def test_invalid_start_node():
    graph = {
        'A': ['B', 'C'],
        'B': ['A'],
        'C': ['B']
    }
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        find_shortest_path(graph, 'X', 'A')

def test_invalid_end_node():
    graph = {
        'A': ['B', 'C'],
        'B': ['A'],
        'C': ['B']
    }
    with pytest.raises(ValueError, match="End node X not found in graph"):
        find_shortest_path(graph, 'A', 'X')

def test_empty_graph():
    graph = {}
    with pytest.raises(ValueError, match="Start node A not found in graph"):
        find_shortest_path(graph, 'A', 'B')

def test_multiple_shortest_paths():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    path = find_shortest_path(graph, 'A', 'D')
    assert path in [['A', 'B', 'D'], ['A', 'C', 'D']]