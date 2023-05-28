import argparse
from pathlib import Path
from shutil import copy2
from time import time


def sorting(source_folder, output_folder):
    for file_path in source_folder.glob('**/*'):
        if file_path.is_file():
            new_folder = output_folder / file_path.suffix[1:]
            new_folder.mkdir(parents=True, exist_ok=True)

            copy2(file_path, new_folder)

    print("Files have been sorted")


def main():
    time_start = time()
    parser = argparse.ArgumentParser(description="Sorting folder")
    parser.add_argument("--source", "-s", help="Source folder", default="picture")
    parser.add_argument("--output", "-o", help="Output folder", default="dist")

    args = vars(parser.parse_args())

    source_folder = Path(args.get("source"))
    output_folder = Path(args.get("output"))
    sorting(source_folder, output_folder)
    time_end = time()
    print(f"Execution time: {time_end - time_start}")


if __name__ == "__main__":
    main()


