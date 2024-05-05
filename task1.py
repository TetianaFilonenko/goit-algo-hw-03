import os
import shutil
import sys


def copy_files(src, dest):
    try:
        os.makedirs(dest, exist_ok=True)

        src_files = os.listdir(src)
        for file_name in src_files:
            full_file_name = os.path.join(src, file_name)

            if os.path.isfile(full_file_name):
                extension = os.path.splitext(file_name)[1].lstrip(".").lower()
                if not extension:
                    extension = "no_extension"
                dest_subdir = os.path.join(dest, extension)
                os.makedirs(dest_subdir, exist_ok=True)

                shutil.copy(full_file_name, dest_subdir)
            elif os.path.isdir(full_file_name):
                copy_files(full_file_name, dest)
    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python task1.py <source_directory> [<destination_directory>]")
        sys.exit(1)

    src_directory = sys.argv[1]
    if len(sys.argv) >= 3:
        dest_directory = sys.argv[2]
    else:
        dest_directory = "dest"

    copy_files(src_directory, dest_directory)


if __name__ == "__main__":
    main()
