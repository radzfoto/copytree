from pathlib import Path
import shutil

debug:bool = False

source_path: Path = Path("/mnt/md0/media/pictures")
dest_path: Path = Path("/mnt/md0/media/photos_raw")

def compare_trees(source_root_path: Path, destination_root_path: Path, check_dirs_only: bool):
    if debug:
        file_counter = 0

    for source_file in source_root_path.rglob("*"):
        if source_file.is_dir():
            relative_path: Path = source_file.relative_to(source_root_path)
            destination_file: Path = destination_root_path / relative_path
            destination_directory: Path = destination_file.parent
        if source_file.is_file():
            relative_path: Path = source_file.relative_to(source_root_path)
            destination_file: Path = destination_root_path / relative_path
            
            destination_directory: Path = destination_file.parent
            dir_created = 1  # Anything that is not None
            if not (destination_directory.exists() and destination_directory.is_dir()):
                dir_created = destination_directory.mkdir(parents=True, exist_ok=True)
            if dir_created is None:
                print(f"mkdir succeeded for directory: {str(destination_directory)}")
            elif destination_directory.exists() and destination_directory.is_dir():
                print(f"mkdir directory exists: {str(destination_directory)}")
            elif destination_directory.exists() and not destination_directory.is_dir():
                print(f"Is not a directory: {str(destination_directory)}")
            else:
                print(f"mkdir failed to create directory: {str(destination_directory)}")
            copy_with_check(Path(source_file), Path(destination_file))
                    
            if debug:
                file_counter += 1
                # Just test copy with a couple of files
                if file_counter == 100:
                    break
        else:
            print("Source file does not exist: " + str(source_file))


def main():
    if debug:
        source_path: Path = Path("/mnt/495a629d-7875-4458-a12c-11eb0fef7b9d/Users/Raul/media/pictures")
        dest_path: Path = Path("/mnt/495a629d-7875-4458-a12c-11eb0fef7b9d/Users/Raul/media/photos_raw")


    copy_matching_files(source_path, dest_path, filter_expression)


if __name__ == "__main__":
    main()