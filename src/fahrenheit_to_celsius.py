def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float or int): Temperature in Fahrenheit.

    Returns:
        float: Temperature converted to Celsius.

    Raises:
        TypeError: If input is not a number (int or float).
    """
    # Check if input is a number
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Input must be a number (int or float)")
    
    # Convert Fahrenheit to Celsius using the standard formula
    # Formula: (°F - 32) × 5/9 = °C
    celsius = (fahrenheit - 32) * 5/9
    
    return round(celsius, 2)  # Round to 2 decimal places for precision