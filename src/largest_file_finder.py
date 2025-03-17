import os
from typing import Union, Optional

def find_largest_file(directory: str) -> Optional[str]:
    """
    Find the largest file in a given directory.

    Args:
        directory (str): Path to the directory to search for the largest file.

    Returns:
        Optional[str]: Path to the largest file, or None if no files exist or 
                       directory is invalid.

    Raises:
        ValueError: If the provided path is not a directory.
    """
    # Validate input is a directory
    if not os.path.exists(directory):
        raise ValueError(f"Directory does not exist: {directory}")
    
    if not os.path.isdir(directory):
        raise ValueError(f"Provided path is not a directory: {directory}")
    
    # Initialize variables to track largest file
    largest_file_path = None
    largest_file_size = 0
    
    # Walk through directory and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip if not a file or cannot be accessed
            try:
                current_file_size = os.path.getsize(file_path)
            except (OSError, IOError):
                continue
            
            # Update largest file if current file is larger
            if current_file_size > largest_file_size:
                largest_file_path = file_path
                largest_file_size = current_file_size
    
    return largest_file_path