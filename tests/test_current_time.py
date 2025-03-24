import pytest
from datetime import datetime
import re
from src.current_time import get_current_time_formatted

def test_current_time_format():
    """
    Test that the function returns a time string in the correct format HH:MM:SS
    """
    # Get the formatted time
    time_str = get_current_time_formatted()
    
    # Check that the string matches the HH:MM:SS format
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', time_str), \
        f"Time format should be HH:MM:SS, got {time_str}"

def test_current_time_values():
    """
    Test that the returned time values are within valid ranges
    """
    # Get the formatted time
    time_str = get_current_time_formatted()
    
    # Split the time string into hours, minutes, seconds
    hours, minutes, seconds = map(int, time_str.split(':'))
    
    # Check each component is within valid range
    assert 0 <= hours < 24, f"Hours should be 0-23, got {hours}"
    assert 0 <= minutes < 60, f"Minutes should be 0-59, got {minutes}"
    assert 0 <= seconds < 60, f"Seconds should be 0-59, got {seconds}"

def test_current_time_consistent():
    """
    Verify that multiple calls within a short time frame are consistent
    """
    # Get time twice in quick succession
    time1 = get_current_time_formatted()
    time2 = get_current_time_formatted()
    
    # They might not be exactly the same if called at different seconds
    # But at least they should be in the same format
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', time1), "First call invalid format"
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', time2), "Second call invalid format"