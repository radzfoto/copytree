from pathlib import Path
import shutil

source_path: Path = Path("/mnt/md0/media/pictures")
dest_path: Path = Path("mnt/md0/media/photos_raw")
filter_expression: str = "*.nef"

def copy_with_check(source_path: Path, destination_path: Path):
    if source_path.is_file():
        try:
            copied_destination = shutil.copy2(source_path, destination_path)
            if destination_path.resolve() == copied_destination:
                print(f"Copy successful: {copied_destination}")
            else:
                print("Copy failed or destination not found for: " + str(destination_path))
        except Exception as e:
            print(f"Error during copy: {e}")
    else:
        print("Source file does not exist: " + str(source_path))



def copy_matching_files(source_root_path: Path, destination_root_path: Path, pattern: str):
    for source_file in source_root_path.rglob(pattern):
        if source_file.is_file():
            relative_path = source_file.relative_to(source_root_path)
            destination_file = destination_root_path / relative_path
            
            destination_file.parent.mkdir(parents=True, exist_ok=True)
            copy_with_check(Path(source_file), Path(destination_file))
        else:
            print("Source file does not exist: " + str(source_file))

def main():
    copy_matching_files(source_path, dest_path, filter_expression)


if __name__ == "__main__":
    main()