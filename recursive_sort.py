from pathlib import Path
import argparse
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description='Sort files in different directories')
    parser.add_argument('-s', '--source', type=Path, required=True,
                        help='directory with unsorted files')
    parser.add_argument('-d', '--destination', type=Path, default=Path("output/"),
                        help='directory for sorted files')
    return parser.parse_args()

def recursive_sort(source: Path, destination: Path):
    try:
        for item in source.iterdir():
            if item.is_dir():
                recursive_sort(item, destination)
            elif item.is_file():
                try:
                    ext = item.suffix.lower().strip('.') or 'no_extension'
                    ext_dir = destination / ext
                    ext_dir.mkdir(exist_ok=True, parents=True)

                    shutil.copy(item, ext_dir / item.name)
                except Exception as file_err:
                    print(f"Error copying file {item}: {file_err}")
    except Exception as dir_err:
        print(f"Error processing directory {source}: {dir_err}")


def main():
    args = parse_args()
    recursive_sort(args.source, args.destination)
    print(args)

if __name__ == "__main__":
    main()