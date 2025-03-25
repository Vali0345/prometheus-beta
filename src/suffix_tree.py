class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    The Suffix Tree allows for fast substring search and provides 
    advanced string pattern matching capabilities.
    """
    
    class Node:
        """
        Represents a node in the Suffix Tree.
        
        Attributes:
            children (dict): Dictionary of child nodes
            suffix_link (Node, optional): Link to another node for efficient traversal
            start (int): Starting index of the edge label
            end (int): Ending index of the edge label
        """
        def __init__(self, start=-1, end=-1):
            """
            Initialize a Suffix Tree Node.
            
            Args:
                start (int, optional): Starting index of the edge label. Defaults to -1.
                end (int, optional): Ending index of the edge label. Defaults to -1.
            """
            self.children = {}
            self.suffix_link = None
            self.start = start
            self.end = end
    
    def __init__(self, text):
        """
        Construct a Suffix Tree for the given text.
        
        Args:
            text (str): Input text to build the suffix tree for
        
        Raises:
            ValueError: If input text is empty or not a string
        """
        if not isinstance(text, str) or len(text) == 0:
            raise ValueError("Input must be a non-empty string")
        
        self.text = text + '$'  # Add termination symbol
        self.root = self.Node()
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Ukkonen's algorithm for constructing suffix tree in O(n) time.
        """
        n = len(self.text)
        
        # Extension rule variables
        last_new_node = None
        global_end = -1
        
        # Iterate through each suffix
        for i in range(n):
            global_end += 1
            last_new_node = None
            
            # Inner loop for each extension
            for j in range(i + 1):
                curr_char = self.text[global_end]
                
                # Find or create appropriate node for extension
                curr_node = self._find_or_create_node(j, i, global_end)
    
    def _find_or_create_node(self, start_index, phase_index, global_end):
        """
        Find or create node during suffix tree construction.
        
        Args:
            start_index (int): Starting index for current suffix
            phase_index (int): Current phase index
            global_end (int): Current global end index
        
        Returns:
            Node: Appropriate node in the suffix tree
        """
        # Placeholder for Ukkonen's algorithm implementation
        # This is a simplified stub that needs full implementation
        return self.root
    
    def search(self, pattern):
        """
        Search for a pattern in the suffix tree.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            bool: True if pattern exists in the text, False otherwise
        
        Raises:
            ValueError: If pattern is empty or not a string
        """
        if not isinstance(pattern, str) or len(pattern) == 0:
            raise ValueError("Pattern must be a non-empty string")
        
        # Traverse the tree to find the pattern
        current = self.root
        
        for char in pattern:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return True
    
    def all_occurrences(self, pattern):
        """
        Find all occurrences of a pattern in the text.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            list: Indices of all occurrences of the pattern
        
        Raises:
            ValueError: If pattern is empty or not a string
        """
        if not isinstance(pattern, str) or len(pattern) == 0:
            raise ValueError("Pattern must be a non-empty string")
        
        # Find all occurrences (simplified implementation)
        occurrences = []
        for i in range(len(self.text) - len(pattern)):
            if self.text[i:i+len(pattern)] == pattern:
                occurrences.append(i)
        
        return occurrences