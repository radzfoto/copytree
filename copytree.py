from pathlib import Path
import shutil

debug:bool = True

def copy_with_check(source_path: Path, destination_path: Path):
    if source_path.is_file():
        try:
            # copied_destination = shutil.copy2(str(source_path), str(destination_path))
            source_path_as_posix: str = source_path.as_posix()
            destination_path_as_posix: str = destination_path.as_posix()
            shutil.copy2(source_path_as_posix, destination_path_as_posix)
            if destination_path.exists():
                print(f"Copy successful: {str(destination_path)}")
            else:
                print("Copy failed or destination not found for: " + str(destination_path))
        except Exception as e:
            print(f"Error during copy: {e}")
    else:
        print("Source file does not exist: " + str(source_path))



def copy_matching_files(source_root_path: Path, destination_root_path: Path, pattern: str):
    if debug:
        file_counter = 0

    for source_file in source_root_path.rglob(pattern):
        if source_file.is_file():
            relative_path: Path = source_file.relative_to(source_root_path)
            destination_file: Path = destination_root_path / relative_path
            
            destination_directory: Path = destination_file.parent
            dir_created = destination_directory.mkdir(parents=True, exist_ok=True)
            if dir_created is None:
                print(f"mkdir succeeded for directory: {str(destination_directory)}")
            if destination_directory.exists():
                print(f"mkdir directory exists: {str(destination_directory)}")
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
    filter_expression: str = "*.nef"
    source_path: Path = Path("/mnt/md0/media/pictures")
    dest_path: Path = Path("/mnt/md0/media/photos_raw")
    if debug:
        source_path: Path = Path("/mnt/495a629d-7875-4458-a12c-11eb0fef7b9d/Users/Raul/media/pictures")
        dest_path: Path = Path("/mnt/495a629d-7875-4458-a12c-11eb0fef7b9d/Users/Raul/media/photos_raw")


    copy_matching_files(source_path, dest_path, filter_expression)


if __name__ == "__main__":
    main()