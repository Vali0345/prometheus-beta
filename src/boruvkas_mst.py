from typing import List, Tuple, Dict

class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure for Boruvka's algorithm
    Helps track connected components efficiently
    """
    def __init__(self, vertices: int):
        """
        Initialize disjoint set with given number of vertices
        
        Args:
            vertices (int): Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item: int) -> int:
        """
        Find the root of a vertex with path compression
        
        Args:
            item (int): Vertex to find the root for
        
        Returns:
            int: Root vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x: int, y: int) -> bool:
        """
        Union two sets by rank
        
        Args:
            x (int): First vertex
            y (int): Second vertex
        
        Returns:
            bool: True if union was successful, False if already in same set
        """
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return False

        # Union by rank
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        
        return True

def boruvkas_mst(vertices: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Implement Boruvka's algorithm to find Minimum Spanning Tree (MST)
    
    Args:
        vertices (int): Number of vertices in the graph
        edges (List[Tuple[int, int, int]]): List of edges with (src, dest, weight)
    
    Returns:
        List[Tuple[int, int, int]]: Edges in the minimum spanning tree
    
    Raises:
        ValueError: If not enough edges to form MST or graph is not connected
    """
    # Edge case: empty graph
    if vertices <= 0:
        return []

    # Sort edges by weight 
    edges.sort(key=lambda x: x[2])

    # Initialize disjoint set
    ds = DisjointSet(vertices)
    
    # Track MST edges
    mst_edges = []
    
    # Track forest/components
    components = vertices

    while components > 1:
        # Track cheapest edges for each component
        cheapest = [None] * vertices

        # Find cheapest edge for each component
        for u, v, w in edges:
            set1 = ds.find(u)
            set2 = ds.find(v)

            if set1 != set2:
                if cheapest[set1] is None or cheapest[set1][2] > w:
                    cheapest[set1] = (u, v, w)
                
                if cheapest[set2] is None or cheapest[set2][2] > w:
                    cheapest[set2] = (u, v, w)

        # Add the cheapest edge for each component
        for edge in cheapest:
            if edge is not None:
                u, v, w = edge
                if ds.union(u, v):
                    mst_edges.append((u, v, w))
                    components -= 1

    # Check if MST is possible
    if len(mst_edges) != vertices - 1:
        raise ValueError("Graph is not connected. Cannot form a Minimum Spanning Tree.")

    return mst_edges