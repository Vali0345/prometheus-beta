from typing import List

def is_bipartite(graph: List[List[int]]) -> bool:
    """
    Check if a graph is bipartite using a two-coloring approach.
    
    A graph is bipartite if its vertices can be divided into two disjoint sets 
    such that every edge connects a vertex in one set to a vertex in the other.
    
    Args:
        graph (List[List[int]]): An adjacency list representation of the graph
                                 where graph[v] contains the list of neighbors of vertex v
    
    Returns:
        bool: True if the graph is bipartite, False otherwise
    
    Raises:
        ValueError: If the input graph is None or not a valid adjacency list
    """
    # Validate input
    if graph is None:
        raise ValueError("Graph cannot be None")
    
    # Empty or single vertex graph is trivially bipartite
    if len(graph) <= 1:
        return True
    
    # Number of vertices
    n = len(graph)
    
    # Color array to track vertex coloring 
    # 0: uncolored, 1: first color group, -1: second color group
    colors = [0] * n
    
    def dfs_color(vertex: int, color: int) -> bool:
        """
        Depth-first search coloring to check bipartiteness
        
        Args:
            vertex (int): Current vertex to color
            color (int): Color to assign (1 or -1)
        
        Returns:
            bool: True if coloring is possible without conflicts
        """
        # Color the current vertex
        colors[vertex] = color
        
        # Check all neighbors
        for neighbor in graph[vertex]:
            # Vertex cannot connect to itself in bipartite graph
            if neighbor == vertex:
                return False
            
            # If neighbor is uncolored, color with opposite color
            if colors[neighbor] == 0:
                if not dfs_color(neighbor, -color):
                    return False
            # If neighbor has same color, graph is not bipartite
            elif colors[neighbor] == color:
                return False
        
        return True
    
    # Check each connected component
    for start in range(n):
        # Skip already colored vertices
        if colors[start] != 0:
            continue
        
        # Color this component
        if not dfs_color(start, 1):
            return False
    
    return True