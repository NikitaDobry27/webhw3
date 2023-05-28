import argparse
import concurrent.futures
import logging
from pathlib import Path
from shutil import copy2
from time import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def sorting(source_folder, output_folder):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for file_path in source_folder.glob('**/*'):
            if file_path.is_file():
                new_folder = output_folder / file_path.suffix[1:]
                new_folder.mkdir(parents=True, exist_ok=True)
                executor.submit(move_file, file_path, new_folder)




def move_file(file_path, new_folder):
    copy2(file_path, new_folder)

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
    logging.info(f"Execution time: {time_end - time_start}")
    logging.info("Files have been sorted")

if __name__ == "__main__":
    main()


