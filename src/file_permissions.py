import os
import stat

def change_file_permissions(file_path, permissions):
    """
    Change the permissions of a file.

    Args:
        file_path (str): Path to the file whose permissions will be changed.
        permissions (int): Octal representation of the desired file permissions.
                           e.g., 0o755 (owner read/write/execute, group/others read/execute)

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permission to change file permissions.
        TypeError: If inputs are of incorrect type.
        ValueError: If permissions are invalid.
    """
    # Input validation
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(permissions, int):
        raise TypeError("permissions must be an integer")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check if permissions are valid (between 0 and 0o777)
    if permissions < 0 or permissions > 0o777:
        raise ValueError("Permissions must be between 0 and 0o777")
    
    try:
        # Change file permissions
        os.chmod(file_path, permissions)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to modify {file_path}")
    
    return True  # Indicate successful permission change