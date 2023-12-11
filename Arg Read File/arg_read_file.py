import os
import argparse

create = argparse.ArgumentParser(
        description="CLI for read file ."
        )
create.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="File Name ."
        )
args = create.parse_args()
os.system(f"cat {args.name}")

