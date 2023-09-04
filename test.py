from pathlib import Path
import shutil

def copy_with_check(source_path: Path, destination_path: Path):
    if source_path.is_file():
        print("Source file exists: " + str(source_path))
        destination_path.parent.mkdir(parents=True, exist_ok=True)
        if (destination_path.parent.is_dir()):
            print("Successfully created: " + str(destination_path.parent))
        else:
            print("Could not create directory: " + str(destination_path.parent))
            return
        
        try:
            print("Attempting to copy file: " + str(source_path) + "\nto: " + destination_path)
            copied_destination = shutil.copy2(source_path, destination_path)
            if destination_path.resolve() == copied_destination:
                print(f"Copy successful: {copied_destination}")
            else:
                print("Copy failed or destination not found for: " + str(destination_path))
        except Exception as e:
            print(f"Error during copy: {e}")
    else:
        print("Source file does not exist: " + str(source_path))

def main():

    source_path: Path = Path("mnt/md0/media/pictures/a.nef")
    dest_path: Path = Path("mnt/md0/media/photos_raw/a.nef")
    copy_with_check(source_path, dest_path)

    source_path: Path = Path("mnt/md0/media/pictures/Fotos Artwork/Artwork/2012-01-21 Around Palo Alto California DSC_2789.nef")
    dest_path: Path = Path("mnt/md0/media/photos_raw/Fotos Artwork/Artwork/2012-01-21 Around Palo Alto California DSC_2789.nef")
    copy_with_check(source_path, dest_path)


if __name__ == "__main__":
    main()