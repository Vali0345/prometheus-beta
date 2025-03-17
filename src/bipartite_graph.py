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
    
    # Color array to track vertex coloring (-1: uncolored, 0: first color, 1: second color)
    colors = [-1] * n
    
    def has_odd_cycle(start: int) -> bool:
        """
        Check if the graph component contains an odd cycle.
        
        Args:
            start (int): Starting vertex for traversal
        
        Returns:
            bool: True if an odd cycle is found, False otherwise
        """
        # Initialize start vertex color
        colors[start] = 0
        queue = [(start, 0)]
        
        while queue:
            current, depth = queue.pop(0)
            
            # Check neighbors
            for neighbor in graph[current]:
                # If neighbor is uncolored
                if colors[neighbor] == -1:
                    # Color with alternate color
                    colors[neighbor] = 1 - colors[current]
                    queue.append((neighbor, depth + 1))
                # If neighbor is colored
                else:
                    # Check for conflict 
                    if colors[neighbor] == colors[current]:
                        return True  # Odd cycle detected
        
        return False
    
    # Traverse all components 
    for start in range(n):
        # Skip if already colored 
        if colors[start] != -1:
            continue
        
        # If current component has an odd cycle, graph is not bipartite
        if has_odd_cycle(start):
            return False
    
    return True