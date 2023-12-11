import argparse
import sys
import requests
import re

def get_url_status(url):
    try:
        response = requests.head(url)
        status_code = response.status_code
        return f"{url} [{status_code} {response.reason}]"
    except requests.RequestException as e:
        return f"{url} [Error: {e}]"

def find_and_check_urls_in_file(file_path):

    url_pattern = r'\b(?:https?|ftp):\/\/[-A-Za-z0-9+&@#\/%?=~_|!:,.;]*[-A-Za-z0-9+&@#\/%=~_|]'

    if file_path is None:
        content = sys.stdin.read()
    else:
        with open(file_path, 'r') as file:
            content = file.readlines()

    urls = re.findall(url_pattern, content)

    urls_with_status = [get_url_status(url) for url in urls]

    return urls_with_status


def main():
    parser = argparse.ArgumentParser(description='Filter lines containing a specific URL and HTTP Status .')
    parser.add_argument('--file', help='Path to the input file. If not provided, reads from standard input.')

    args = parser.parse_args()

    urls_with_status = find_and_check_urls_in_file(args.file)

    for line in urls_with_status:
        print(line)

if __name__ == '__main__':
    main()


