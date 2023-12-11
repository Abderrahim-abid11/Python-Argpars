import os
import argparse

create = argparse.ArgumentParser(
        description="CLI for Update file Name ."
        )
create.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="File Name ."
        )
create.add_argument(
        "-c", "--copyname", metavar="copyname",
        required=True, help="Copy File Name ."
        )
args = create.parse_args()
os.system(f"cp {args.name} {args.copyname}")

print("\n")
print("file copyed .")
