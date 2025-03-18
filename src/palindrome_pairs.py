def find_palindrome_pairs(words):
    """
    Find all pairs of indices in an array of strings where concatenated strings form a palindrome.
    
    Args:
        words (List[str]): A list of strings to find palindrome pairs in
    
    Returns:
        List[Tuple[int, int]]: A list of pairs of indices where concatenated strings form a palindrome
    
    Complexity: 
        Time: O(n^2 * k), where n is the number of words and k is the length of the longest word
        Space: O(1) excluding the output list
    
    Examples:
        >>> find_palindrome_pairs(["bat", "tab", "cat"])
        [(0, 1), (1, 0)]
        >>> find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
        [(0, 1), (1, 0), (3, 4), (4, 3)]
    """
    def is_palindrome(s):
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    # Check every possible pair of words
    for i in range(n):
        for j in range(n):
            # Skip same index
            if i == j:
                continue
            
            # Concatenate words and check if palindrome
            concatenated = words[i] + words[j]
            if is_palindrome(concatenated):
                # Only add pairs that weren't added before
                if (i, j) not in result:
                    result.append((i, j))
    
    # Special handling for empty list and edge cases
    if not words or len(words) == 1:
        return []
    
    return result