from pathlib import Path
import shutil

debug:bool = False

#filter_expression: str = "*.nef"
#filter_expression: str = "*.NEF"
#filter_expression: str = "*.psd"
#filter_expression: str = "*.PSD"
#filter_expression: str = "*.cr2"
#filter_expression: str = "*.CR2"
#filter_expression: str = "*.tif"
#filter_expression: str = "*.TIF"
#filter_expression: str = "*.xcf"
#filter_expression: str = "*.cxf"
#filter_expression: str = "*.zip"
#filter_expression: str = "*.ZIP"
pattern_list = ["*.nef", "*.NEF", "*.psd", "*.PSD", "*.cr2", "*.CR2", "*.tif", "*.TIF", "*.xcf", "*.cxf", "*.zip", "*.ZIP"]

source_path: Path = Path("/mnt/md0/media/pictures")
#dest_path: Path = Path("/mnt/md0/media/photos_raw")

def delete_files_matching_pattern(directory_path: Path, pattern: str):
    # Iterate through all files matching the pattern recursively
    for file_path in directory_path.rglob(pattern):
        if file_path.is_file():
            # Delete the file
            file_path.unlink()
            print(f"Deleted: {str(file_path)}")

def main():
    if debug:
        source_path: Path = Path("/mnt/495a629d-7875-4458-a12c-11eb0fef7b9d/Users/Raul/media/pictures")
        #dest_path: Path = Path("/mnt/495a629d-7875-4458-a12c-11eb0fef7b9d/Users/Raul/media/photos_raw")

    for pattern in pattern_list:
        delete_files_matching_pattern(source_path, pattern)


if __name__ == "__main__":
    main()