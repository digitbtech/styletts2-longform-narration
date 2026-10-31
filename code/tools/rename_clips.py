import os

def rename_files_numberwise(directory, prefix="wav-", padding=4):
    # Get all files (excluding subdirectories)
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Sort files alphabetically to ensure consistent ordering
    files.sort()

    for i, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]  # Keep original file extension
        new_name = f"{prefix}{str(i).zfill(padding)}{ext}"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

# Example usage:
rename_files_numberwise("AudioSet_Phase2/wavs")