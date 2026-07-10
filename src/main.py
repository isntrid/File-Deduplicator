from pathlib import Path

class File:
    def __init__(self, size, modified_time, creation_time):
        self.size = size
        self.modified_time = modified_time
        self.creation_time = creation_time

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
            path = directory.resolve()
        else:
            print("Directory not found; did you spell it correctly?")

def convert_files():
    files = list(dir.iterdir())
    for file in files:
        path = file.stat()
        size = path.st_size, modified_time = path.st_mtime, creation_time = path.st_ctime
        File(size=size, modified_time=modified_time, creation_time=creation_time)



def main():
    pass


