import random
from typing import List, Dict, Union

class MountainPeak:
    """
    Represents a mountain peak with its characteristics.
    
    Attributes:
        name (str): Name of the mountain peak
        height (float): Height of the mountain peak in meters
        latitude (float): Latitude coordinate of the peak
        longitude (float): Longitude coordinate of the peak
    """
    def __init__(self, name: str, height: float, latitude: float, longitude: float):
        """
        Initialize a mountain peak.
        
        Args:
            name (str): Name of the mountain peak
            height (float): Height of the mountain peak in meters
            latitude (float): Latitude coordinate of the peak
            longitude (float): Longitude coordinate of the peak
        """
        self.name = name
        self.height = height
        self.latitude = latitude
        self.longitude = longitude

def create_mountain_range(num_peaks: int) -> List[MountainPeak]:
    """
    Generate a list of mountain peaks with specified number of peaks.
    
    Args:
        num_peaks (int): Number of mountain peaks to generate
    
    Returns:
        List[MountainPeak]: A list of generated mountain peaks
    
    Raises:
        ValueError: If num_peaks is less than 1
    """
    # Validate input
    if num_peaks < 1:
        raise ValueError("Number of peaks must be at least 1")
    
    # Predefined list of mountain range names to sample from
    mountain_names = [
        "Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu", 
        "Cho Oyu", "Dhaulagiri", "Manaslu", "Nanga Parbat", "Annapurna",
        "Mont Blanc", "Matterhorn", "Eiger", "Jungfrau", "Monte Rosa",
        "McKinley", "Denali", "Rainier", "Hood", "Whitney"
    ]
    
    # Generate mountain peaks
    mountain_range = []
    used_names = set()
    
    for _ in range(num_peaks):
        # Ensure unique names
        while True:
            name = random.choice(mountain_names)
            if name not in used_names:
                used_names.add(name)
                break
        
        # Generate random characteristics
        height = round(random.uniform(1000, 8848), 2)  # Height between 1000m and 8848m (Everest height)
        latitude = round(random.uniform(-90, 90), 4)
        longitude = round(random.uniform(-180, 180), 4)
        
        # Create and add mountain peak
        peak = MountainPeak(name, height, latitude, longitude)
        mountain_range.append(peak)
    
    return mountain_range