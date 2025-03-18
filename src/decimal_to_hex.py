def decimal_to_hex(decimal_num):
    """
    Convert a decimal number to its hexadecimal representation.

    Args:
        decimal_num (int): The decimal number to convert.

    Returns:
        str: The hexadecimal representation of the input number.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    # Check input type
    if not isinstance(decimal_num, int):
        raise TypeError("Input must be an integer")
    
    # Check for negative numbers
    if decimal_num < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for zero
    if decimal_num == 0:
        return "0"
    
    # Hexadecimal conversion digits
    hex_digits = "0123456789ABCDEF"
    
    # Store the hexadecimal representation
    hex_num = ""
    
    # Convert decimal to hexadecimal
    while decimal_num > 0:
        # Get the remainder when divided by 16
        remainder = decimal_num % 16
        
        # Prepend the corresponding hex digit
        hex_num = hex_digits[remainder] + hex_num
        
        # Integer division by 16
        decimal_num //= 16
    
    return hex_num