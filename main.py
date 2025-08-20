from pathlib import Path
from shutil import move

file_source = Path(r"/home/ryanward/Desktop/tempSource")
file_dest = Path(r"/home/ryanward/Desktop/tempDest")
file_dest.mkdir(parents=True, exist_ok=True)
file_path_jpg = Path(r"/home/ryanward/Desktop/tempDest/jpg")
file_path_jpg.mkdir(parents=True, exist_ok=True)
file_path_raw = Path(r"/home/ryanward/Desktop/tempDest/raw")
file_path_raw.mkdir(parents=True, exist_ok=True)

def photo_sort(file_source, file_dest):

    for file in file_source.iterdir():
        # Skip hidden directory files.
        if file.name.startswith('.'):
            continue
        else:
            print(f"Processing: {file.name}, type: {file.suffix}")

            if file.suffix.lower() == '.jpg':
                move(file, file_path_jpg)
            elif file.suffix.lower() == '.raf':
                move(file, file_path_raw)
            else:
                print("file wrong type")

photo_sort(file_source, file_dest)
