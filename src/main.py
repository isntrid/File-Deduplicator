from pathlib import Path

class File:
    def __init__(self, path):
        self.size = path.st_size
        self.modified_time = path.st_mtime
        self.creation_time = path.st_ctime

    def __repr__(self):
        return f"size={self.size}, modified={self.modified_time}, created={self.creation_time})"

    def __eq__(self, other):
        return self.size == other.size and self.modified_time == other.modified_time and self.creation_time == other.creation_time

def set_directory():
    home = Path.home()
    while True:
        #location = input("Enter a directory: ")
        location = "downloads" #temp
        directory = home / location
        if directory.is_dir():
            return directory.resolve()
        else:
            print("Directory not found; did you spell it correctly?")

def convert_files():
    files = []
    for file in dir.iterdir():
        path = file.stat()
        new_file = File(path)
        files.append(new_file)
    return files

def compare_files():


def main():
    pass


