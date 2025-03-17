from typing import List, Dict

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
    
    # Number of vertices
    n = len(graph)
    
    # Color array to track vertex coloring (-1: uncolored, 0: first color, 1: second color)
    colors = [-1] * n
    
    # Check each uncolored vertex
    for start in range(n):
        # Skip if already colored
        if colors[start] != -1:
            continue
        
        # Use BFS to color the graph
        colors[start] = 0
        queue = [start]
        
        while queue:
            current = queue.pop(0)
            
            # Check neighbors
            for neighbor in graph[current]:
                # If neighbor is uncolored, color it with opposite color
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[current]
                    queue.append(neighbor)
                # If neighbor has same color as current, graph is not bipartite
                elif colors[neighbor] == colors[current]:
                    return False
    
    return True