import os
import shutil
from pathlib import Path


def copy_files_with_concatenated_path(source_dir: Path, target_dir: Path) -> None:
    for root, dirs, files in os.walk(source_dir):
        if root != source_dir and files:  # Check if there are files in the directory
            # Construct the new subfolder name
            subfolder_name = root.replace(
                source_dir, '').replace(os.sep, '_').strip('_')
            new_folder_path = os.path.join(target_dir, subfolder_name)

            # Only create the subfolder in the target directory if it doesn't exist
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)

            # Copy each file to the new location
            for file in files:
                shutil.copy2(os.path.join(root, file),
                             os.path.join(new_folder_path, file))


# Example usage
SOURCE_DIR = Path(r'C:\Users\You\Desktop\splice new\merged')
TARGET_DIR = Path(r'C:\Users\You\Desktop\Ableton\sorted')
copy_files_with_concatenated_path(SOURCE_DIR, TARGET_DIR)
