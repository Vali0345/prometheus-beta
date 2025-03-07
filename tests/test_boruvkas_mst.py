import pytest
from src.boruvkas_mst import boruvkas_mst, DisjointSet

def test_disjoint_set():
    """Test DisjointSet data structure functionality"""
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union two sets
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    
    # Union more sets
    ds.union(2, 3)
    ds.union(0, 3)
    
    # Check all are now in same set
    assert ds.find(0) == ds.find(1)
    assert ds.find(0) == ds.find(2)
    assert ds.find(0) == ds.find(3)

def test_boruvkas_mst_basic():
    """Test a simple graph with Boruvka's algorithm"""
    vertices = 4
    edges = [
        (0, 1, 10),  # heavy edge
        (0, 2, 6),   # light edge
        (0, 3, 5),   # light edge
        (1, 3, 15),
        (2, 3, 4)    # lightest edge
    ]
    
    mst = boruvkas_mst(vertices, edges)
    
    # Check MST properties
    assert len(mst) == vertices - 1
    
    # Check total weight of MST
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 15  # 6 + 5 + 4

def test_boruvkas_mst_disconnected_graph():
    """Test that an error is raised for disconnected graphs"""
    vertices = 4
    edges = [
        (0, 1, 10),
        (2, 3, 5)
    ]
    
    with pytest.raises(ValueError, match="Graph is not connected"):
        boruvkas_mst(vertices, edges)

def test_boruvkas_mst_empty_graph():
    """Test empty graph scenario"""
    vertices = 0
    edges = []
    
    mst = boruvkas_mst(vertices, edges)
    assert mst == []

def test_boruvkas_mst_single_vertex():
    """Test graph with single vertex"""
    vertices = 1
    edges = []
    
    mst = boruvkas_mst(vertices, edges)
    assert mst == []

def test_boruvkas_mst_complex_graph():
    """Test a more complex graph"""
    vertices = 6
    edges = [
        (0, 1, 4), (0, 2, 4),
        (1, 2, 2), (1, 3, 3),
        (1, 4, 1), (2, 3, 5),
        (2, 5, 6), (3, 4, 2),
        (3, 5, 7), (4, 5, 3)
    ]
    
    mst = boruvkas_mst(vertices, edges)
    
    # Check MST properties
    assert len(mst) == vertices - 1
    
    # Verify connections
    ds = DisjointSet(vertices)
    for u, v, _ in mst:
        ds.union(u, v)
    
    # Ensure all vertices are connected
    for i in range(1, vertices):
        assert ds.find(0) == ds.find(i)