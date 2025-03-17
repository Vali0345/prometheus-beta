from datetime import date

def get_current_date() -> str:
    """
    Returns the current date in YYYY-MM-DD format.

    Returns:
        str: Current date as a string in the format 'YYYY-MM-DD'
    
    Example:
        >>> get_current_date()
        '2023-06-15'
    """
    return date.today().strftime("%Y-%m-%d")