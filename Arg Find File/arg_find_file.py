import os
import argparse

create = argparse.ArgumentParser(
        description="CLI for search about file in current dir ."
        )
create.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="File Name ."
        )
args = create.parse_args()
os.system(f"find . -name {args.name}")

print("\n")
print(".")
