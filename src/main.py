from pathlib import Path

def get_input():
    home = Path.home()
    while True:
        location = input("Enter a directory: ")
        directory = home / location
        if directory.is_dir():
            return directory
        else:
            print("Directory not found, did you spell it correctly?")


def main():
    pass

dir = get_input()
p = list(dir.iterdir())[0]

print(p.stat())