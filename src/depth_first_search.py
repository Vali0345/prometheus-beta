from typing import List, Any, Optional, Set, Callable

def depth_first_search(graph: dict, start: Any, 
                       visit_fn: Optional[Callable[[Any], None]] = None) -> List[Any]:
    """
    Perform Depth-First Search on a graph.

    Args:
        graph (dict): A dictionary representing the graph where keys are nodes 
                      and values are lists of adjacent nodes.
        start (Any): The starting node for the DFS traversal.
        visit_fn (Optional[Callable]): Optional function to call on each node during traversal.

    Returns:
        List[Any]: A list of nodes in the order they were visited.

    Raises:
        ValueError: If the start node is not in the graph.
        TypeError: If the graph is not a dictionary or visit_fn is not callable.
    """
    # Input validation
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary")
    
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    
    if visit_fn is not None and not callable(visit_fn):
        raise TypeError("Visit function must be callable")

    # Initialize data structures
    visited: Set[Any] = set()
    traversal_order: List[Any] = []

    def dfs_recursive(node: Any) -> None:
        """
        Recursive helper function for depth-first search.
        
        Args:
            node (Any): Current node being explored.
        """
        # Mark the current node as visited
        if node in visited:
            return
        
        visited.add(node)
        
        # Optional visit function
        if visit_fn:
            visit_fn(node)
        
        # Add to traversal order
        traversal_order.append(node)
        
        # Explore unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)

    # Start DFS from the given start node
    dfs_recursive(start)

    return traversal_order