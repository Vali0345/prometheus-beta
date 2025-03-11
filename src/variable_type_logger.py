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
        # Logs: Variable type is: <class 'int'>
        >>> log_variable_type("Hello")
        # Logs: Variable type is: <class 'str'>
    """
    # If None was passed, use type(None)
    if variable is None:
        type_str = "<class 'NoneType'>"
        logging.info(f"Variable type is: {type_str}")
        return type(None)

    # Get the type of the variable
    var_type = type(variable)
    type_str = f"<class '{var_type.__name__}'>"
    
    # Log the type
    logging.info(f"Variable type is: {type_str}")
    
    # Return the type for potential further use
    return var_type