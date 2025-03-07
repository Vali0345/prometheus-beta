from typing import Dict, List, Optional, Set

class HopcroftKarp:
    """
    Implementation of the Hopcroft-Karp algorithm for maximum matching in a bipartite graph.
    
    The algorithm finds the maximum matching in a bipartite graph in O(E√V) time complexity.
    
    Attributes:
        graph (Dict[int, List[int]]): Adjacency list representation of the bipartite graph
        matching (Dict[int, Optional[int]]): Stores the current matching
        dist (Dict[int, int]): Distances used in BFS
    """
    
    def __init__(self, graph: Dict[int, List[int]]):
        """
        Initialize the Hopcroft-Karp algorithm.
        
        Args:
            graph (Dict[int, List[int]]): Adjacency list of the bipartite graph
                Keys are nodes from the left set, values are lists of connected nodes in the right set
        """
        if not isinstance(graph, dict):
            raise TypeError("Graph must be a dictionary")
        
        self.graph = graph
        self.matching: Dict[int, Optional[int]] = {}
        self.dist: Dict[int, int] = {}
    
    def _bfs(self, left_nodes: Set[int]) -> bool:
        """
        Breadth-first search to find augmenting paths.
        
        Args:
            left_nodes (Set[int]): Set of unmatched nodes in the left set
        
        Returns:
            bool: True if an augmenting path exists, False otherwise
        """
        queue = []
        
        # Initialize distances
        for u in left_nodes:
            if self.matching.get(u) is None:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        
        self.dist[None] = float('inf')
        
        while queue:
            u = queue.pop(0)
            if self.dist[u] < self.dist[None]:
                for v in self.graph.get(u, []):
                    # Check if matched node or unmatched node
                    w = self.matching.get(v)
                    
                    if w is None or self.dist[w] == float('inf'):
                        if w is None:
                            self.dist[None] = self.dist[u] + 1
                        else:
                            self.dist[w] = self.dist[u] + 1
                            queue.append(w)
        
        return self.dist[None] != float('inf')
    
    def _dfs(self, u: Optional[int]) -> bool:
        """
        Depth-first search to find augmenting paths.
        
        Args:
            u (Optional[int]): Current node in the left set
        
        Returns:
            bool: True if an augmenting path is found, False otherwise
        """
        if u is not None:
            for v in self.graph.get(u, []):
                w = self.matching.get(v)
                
                # Find an augmenting path
                if w is None or (self.dist[w] == self.dist[u] + 1 and self._dfs(w)):
                    self.matching[v] = u
                    self.matching[u] = v
                    return True
            
            # No augmenting path found
            self.dist[u] = float('inf')
            return False
        
        return True
    
    def maximum_matching(self) -> Dict[int, int]:
        """
        Compute the maximum matching in the bipartite graph.
        
        Returns:
            Dict[int, int]: A maximum matching where keys and values are matched nodes
        """
        # Reset matching
        self.matching.clear()
        
        # Get all left nodes
        left_nodes = set(self.graph.keys())
        
        # Repeatedly find augmenting paths
        matching_size = 0
        while self._bfs(left_nodes):
            for u in left_nodes:
                if self.matching.get(u) is None:
                    if self._dfs(u):
                        matching_size += 1
        
        return {k: v for k, v in self.matching.items() if k in left_nodes and v is not None}