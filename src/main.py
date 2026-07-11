from pathlib import Path
import hashlib

class File:
    def __init__(self, path):
        self.path = path
        self.size = path.stat().st_size

    def sha256(self):
        hasher = hashlib.sha256()
        with self.path.open("rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()

    def __repr__(self):
        return f"{self.path.name} ({self.size} bytes)"

def set_directory():
    home = Path.home()
    while True:
        location = input("Enter a directory: ")
        directory = home / location
        if directory.is_dir():
            return directory.resolve()
        else:
            print("Directory not found; did you spell it correctly?")

def convert_files(directory):
    files = []
    for path in directory.iterdir():
        if path.is_file():
            files.append(File(path))
    return files

def compare_files(files):
    size_groups = {}

    for file in files:
        size_groups.setdefault(file.size, []).append(file)

    for group in size_groups.values():
        if len(group) < 2:
            continue

        hash_groups = {}
        for file in group:
            file_hash = file.sha256()
            hash_groups.setdefault(file_hash, []).append(file)

        for duplicates in hash_groups.values():
            if len(duplicates) > 1:
                print("\nDuplicate files found:")

                for file in duplicates:
                    print(file.path)

                answer = input("Would you like to delete the duplicates? y/n: ").strip().lower()

                if answer == "y":
                    for file in duplicates[:1]:
                        try:
                            file.path.unlink()
                            print(f"Deleted: {file.path}")
                        except PermissionError:
                            print(f"Permission denied: {file.path}")
                        except Exception as e:
                            print(f"Failed to delete {file.path}: {e}")
def main():
    directory = set_directory()
    files = convert_files(directory)
    compare_files(files)

if __name__ == "__main__":
    main()