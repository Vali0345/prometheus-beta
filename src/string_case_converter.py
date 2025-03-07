def to_kebab_case(input_string):
    """
    Convert a given string to kebab-case.
    
    Kebab case is a naming convention where words are lowercase and separated by hyphens.
    
    Args:
        input_string (str): The input string to convert to kebab case.
    
    Returns:
        str: The input string converted to kebab case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_kebab_case("Hello World")
        'hello-world'
        >>> to_kebab_case("snake_case_string")
        'snake-case-string'
        >>> to_kebab_case("camelCaseString")
        'camel-case-string'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Convert to lowercase first
    # Replace any non-alphanumeric sequences with a single hyphen
    import re
    
    # Convert camelCase and PascalCase
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', input_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1)
    
    # Replace underscores and multiple spaces with single hyphen
    s3 = re.sub(r'[_\s]+', '-', s2)
    
    # Remove any non-alphanumeric characters except hyphens
    s4 = re.sub(r'[^a-z0-9-]', '', s3.lower())
    
    # Remove consecutive hyphens
    s5 = re.sub(r'-+', '-', s4)
    
    # Remove leading and trailing hyphens
    return s5.strip('-')