import re
from datetime import datetime
import pytest
from src.current_time import get_current_time_formatted

def test_current_time_format():
    """
    Test that the function returns a time string in the correct format.
    """
    # Get the formatted time
    time_str = get_current_time_formatted()
    
    # Validate the format using a regex pattern
    # HH:MM:SS where HH is 00-23, MM and SS are 00-59
    time_pattern = r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$'
    
    # Assert that the time string matches the expected format
    assert re.match(time_pattern, time_str), f"Invalid time format: {time_str}"

def test_current_time_accuracy():
    """
    Test that the function returns a time close to the current time.
    """
    # Get the function's time
    func_time_str = get_current_time_formatted()
    
    # Get the current time
    current_time = datetime.now()
    
    # Format the current time for comparison
    current_time_str = current_time.strftime('%H:%M:%S')
    
    # The times should match (allow for a small potential time difference)
    assert func_time_str == current_time_str