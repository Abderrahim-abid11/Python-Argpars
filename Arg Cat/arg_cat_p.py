import argparse
import sys

def filter_lines(file_path, keyword):
    if file_path is None:
        lines = sys.stdin.readlines()
    else:
        with open(file_path, 'r') as file:
            lines = file.readlines()

    filtered_lines = [line.strip() for line in lines if keyword.lower() in line.lower()]

    return filtered_lines

def main():
    parser = argparse.ArgumentParser(description='Filter lines containing a specific word.')
    parser.add_argument('name', help='Keyword to filter lines')
    parser.add_argument('--file', help='Path to the input file. If not provided, reads from standard input.')

    args = parser.parse_args()

    filtered_lines = filter_lines(args.file, args.name)

    for line in filtered_lines:
        print(line)

if __name__ == '__main__':
    main()

