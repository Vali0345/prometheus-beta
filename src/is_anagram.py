def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once. The function is case-insensitive and 
    ignores whitespace.

    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare

    Returns:
        bool: True if the strings are anagrams, False otherwise

    Raises:
        TypeError: If either input is not a string
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both arguments must be strings")
    
    # Normalize strings by removing whitespace and converting to lowercase
    normalized1 = ''.join(str1.lower().split())
    normalized2 = ''.join(str2.lower().split())
    
    # Check if normalized strings have same length
    if len(normalized1) != len(normalized2):
        return False
    
    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}
    
    # Count character frequencies
    for char in normalized1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in normalized2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare character frequency dictionaries
    return char_count1 == char_count2