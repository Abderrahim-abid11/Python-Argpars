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
        "-nn", "--newname", metavar="newname",
        required=True, help="New File Name ."
        )
args = create.parse_args()
os.system(f"mv {args.name} {args.newname}")

print("\n")
print("file renamed .")
