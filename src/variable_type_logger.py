import logging

def log_variable_type(variable):
    """
    Log the type of a given variable to the console.

    This function uses the logging module to output the type of the input variable.
    It supports logging for any Python object and handles None type as well.

    Args:
        variable (Any): The variable whose type needs to be logged.

    Returns:
        type: The type of the input variable.

    Examples:
        >>> log_variable_type(42)
        # Logs: INFO:root:Variable type is: <class 'int'>
        >>> log_variable_type("Hello")
        # Logs: INFO:root:Variable type is: <class 'str'>
    """
    # Configure basic logging if not already configured
    logging.basicConfig(level=logging.INFO)

    # Handle None separately
    if variable is None:
        logging.info("Variable type is: <class 'NoneType'>")
        return type(None)

    # Log the type of the variable
    logging.info(f"Variable type is: {type(variable)}")
    
    # Return the type for potential further use
    return type(variable)