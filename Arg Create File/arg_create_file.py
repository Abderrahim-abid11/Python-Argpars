import os
import argparse

create = argparse.ArgumentParser(
        description="CLI for create file ."
        )
create.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="File Name ."
        )
args = create.parse_args()
os.system(f"touch {args.name}")

print("\n")
print("file create .")
