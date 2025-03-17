import pytest
from datetime import date
from src.get_current_date import get_current_date

def test_get_current_date_format():
    """
    Test that the returned date matches the expected YYYY-MM-DD format
    and is the current date.
    """
    current_date = get_current_date()
    
    # Check that the string is in the correct format (YYYY-MM-DD)
    assert len(current_date) == 10, "Date string should be 10 characters long"
    assert current_date[4] == '-', "Fifth character should be a hyphen"
    assert current_date[7] == '-', "Eighth character should be a hyphen"
    
    # Verify the date matches today's date
    today = date.today().strftime("%Y-%m-%d")
    assert current_date == today, "Returned date should match today's date"

def test_get_current_date_type():
    """
    Test that the function returns a string.
    """
    result = get_current_date()
    assert isinstance(result, str), "Return value should be a string"