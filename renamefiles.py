import os
from multiprocessing import Pool

def rename_file(args):
    old_file_path, new_file_path = args
    if os.path.exists(new_file_path):
        print(f"Skipping rename for {old_file_path}, as {new_file_path} already exists.")
        return

    try:
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_file_path} to {new_file_path}")
    except OSError as e:
        print(f"Error renaming file {old_file_path}: {e}")

def rename_files(directory, file_names, new_name):
    rename_tasks = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file in file_names:
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, new_name)
                rename_tasks.append((old_file_path, new_file_path))
    
    with Pool() as pool:
        pool.map(rename_file, rename_tasks)

def main():
    directory = input("Enter the directory path: ")
    file_names_input = input("Enter the file names to rename (separated by commas): ")
    file_names = [name.strip() for name in file_names_input.split(',')]
    new_name = input("Enter the new file name: ")

    rename_files(directory, file_names, new_name)

if __name__ == "__main__":
    main()
    