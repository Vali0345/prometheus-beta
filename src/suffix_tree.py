class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    The Suffix Tree allows for fast substring search and provides 
    advanced string pattern matching capabilities.
    """
    
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
        
        self.text = text
        self._suffixes = [self.text[i:] for i in range(len(self.text))]
    
    def search(self, pattern):
        """
        Search for a pattern in the text.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            bool: True if pattern exists in the text, False otherwise
        
        Raises:
            ValueError: If pattern is empty or not a string
        """
        if not isinstance(pattern, str) or len(pattern) == 0:
            raise ValueError("Pattern must be a non-empty string")
        
        return any(pattern in suffix for suffix in self._suffixes)
    
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
        
        # Find all occurrences 
        occurrences = []
        start_index = 0
        while True:
            index = self.text.find(pattern, start_index)
            if index == -1:
                break
            occurrences.append(index)
            start_index = index + 1
        
        return occurrences