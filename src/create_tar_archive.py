import os
import tarfile
from typing import Union, Optional


def create_tar_archive(source_dir: str, 
                       archive_path: Optional[str] = None, 
                       compression: str = 'gz') -> str:
    """
    Create a tar archive of a specified directory.

    Args:
        source_dir (str): Path to the directory to be archived
        archive_path (Optional[str]): Path where the archive will be saved. 
                                      If None, creates archive in same directory as source
        compression (str, optional): Compression type. 
                                     Supports 'gz' (default), 'bz2', or 'xz'

    Returns:
        str: Full path to the created archive

    Raises:
        ValueError: If source directory does not exist or is not a directory
        ValueError: If invalid compression type is specified
    """
    # Validate source directory
    source_dir = os.path.abspath(source_dir)
    if not os.path.exists(source_dir):
        raise ValueError(f"Source directory {source_dir} does not exist")
    if not os.path.isdir(source_dir):
        raise ValueError(f"Source {source_dir} is not a directory")

    # Validate compression type
    valid_compression = {
        'gz': 'w:gz', 
        'bz2': 'w:bz2', 
        'xz': 'w:xz'
    }
    if compression not in valid_compression:
        raise ValueError(f"Invalid compression type. Must be one of {list(valid_compression.keys())}")

    # Determine archive path
    if archive_path is None:
        archive_path = os.path.join(
            os.path.dirname(source_dir), 
            f"{os.path.basename(source_dir)}.tar.{compression}"
        )
    else:
        archive_path = os.path.abspath(archive_path)

    # Create tar archive
    with tarfile.open(archive_path, valid_compression[compression]) as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

    return archive_path