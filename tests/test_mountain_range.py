import pytest
from src.mountain_range import create_mountain_range, MountainPeak

def test_create_mountain_range_basic():
    """Test creating a mountain range with a standard number of peaks."""
    num_peaks = 5
    mountain_range = create_mountain_range(num_peaks)
    
    # Check basic properties
    assert len(mountain_range) == num_peaks
    assert all(isinstance(peak, MountainPeak) for peak in mountain_range)

def test_create_mountain_range_single_peak():
    """Test creating a mountain range with a single peak."""
    num_peaks = 1
    mountain_range = create_mountain_range(num_peaks)
    
    assert len(mountain_range) == 1
    assert isinstance(mountain_range[0], MountainPeak)

def test_create_mountain_range_peak_characteristics():
    """Test the characteristics of generated mountain peaks."""
    num_peaks = 10
    mountain_range = create_mountain_range(num_peaks)
    
    # Check each peak's attributes
    for peak in mountain_range:
        # Name tests
        assert isinstance(peak.name, str)
        assert len(peak.name) > 0
        
        # Height tests
        assert isinstance(peak.height, float)
        assert 1000 <= peak.height <= 8848
        
        # Latitude tests
        assert isinstance(peak.latitude, float)
        assert -90 <= peak.latitude <= 90
        
        # Longitude tests
        assert isinstance(peak.longitude, float)
        assert -180 <= peak.longitude <= 180

def test_create_mountain_range_unique_names():
    """Test that generated mountain ranges have unique names."""
    num_peaks = 20
    mountain_range = create_mountain_range(num_peaks)
    
    names = [peak.name for peak in mountain_range]
    assert len(names) == len(set(names))

def test_create_mountain_range_invalid_input():
    """Test that an error is raised for invalid number of peaks."""
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(0)
    
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(-5)