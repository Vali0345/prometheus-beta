from collections import deque
from typing import List, Dict, Optional, Union

def find_shortest_path(graph: Dict[Union[int, str], List[Union[int, str]]], 
                       start: Union[int, str], 
                       end: Union[int, str]) -> Optional[List[Union[int, str]]]:
    """
    Find the shortest path between start and end nodes in an unweighted graph using BFS.
    
    Args:
        graph (Dict): Adjacency list representing the graph
        start (int/str): Starting node 
        end (int/str): Destination node
    
    Returns:
        Optional[List]: Shortest path from start to end, or None if no path exists
    
    Raises:
        ValueError: If start or end nodes are not in the graph
    """
    # Validate input nodes exist in the graph
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    if end not in graph:
        raise ValueError(f"End node {end} not found in graph")
    
    # Special case: start and end are the same
    if start == end:
        return [start]
    
    # Queue for BFS
    queue = deque([(start, [start])])
    
    # Track visited nodes to prevent cycles
    visited = set([start])
    
    # BFS traversal
    while queue:
        current_node, path = queue.popleft()
        
        # Check neighbors
        for neighbor in graph.get(current_node, []):
            # Skip already visited nodes
            if neighbor in visited:
                continue
            
            # New path to this neighbor
            new_path = path + [neighbor]
            
            # Found the destination
            if neighbor == end:
                return new_path
            
            # Mark as visited and add to queue
            visited.add(neighbor)
            queue.append((neighbor, new_path))
    
    # No path found
    return None