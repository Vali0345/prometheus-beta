def simple_calculator(num1, num2, operator):
    """
    Perform basic arithmetic operations on two numbers.

    Args:
        num1 (float): The first number in the calculation.
        num2 (float): The second number in the calculation.
        operator (str): The arithmetic operation to perform.
                        Supports '+', '-', '*', '/' operations.

    Returns:
        float: The result of the arithmetic operation.

    Raises:
        ValueError: If an invalid operator is provided.
        ZeroDivisionError: If division by zero is attempted.
    """
    # Convert inputs to float to support decimal calculations
    num1 = float(num1)
    num2 = float(num2)

    # Perform calculation based on the operator
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check for division by zero
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2
    else:
        # Raise error for unsupported operators
        raise ValueError(f"Unsupported operator: {operator}. Supported operators are '+', '-', '*', '/'")