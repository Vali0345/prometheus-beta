def reverse_word_order(s: str) -> str:
    """
    Reverse the order of words in a string while preserving original capitalization and punctuation.
    
    Args:
        s (str): The input string to be processed.
    
    Returns:
        str: A new string with words reversed, maintaining original case and punctuation.
    
    Examples:
        >>> reverse_word_order("Hello World!")
        'World! Hello'
        >>> reverse_word_order("Python is AWESOME.")
        'AWESOME. is Python'
        >>> reverse_word_order("a b c")
        'c b a'
    """
    # Handle empty string or single word cases
    if not s or len(s.split()) <= 1:
        return s
    
    # Split the string into words
    words = s.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Reconstruct the string to maintain original spacing and punctuation
    return ' '.join(reversed_words)