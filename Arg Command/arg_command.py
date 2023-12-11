import os
import argparse

command = argparse.ArgumentParser(
        description="CLI for execute command line shell ."
        )

command.add_argument(
        "-c", "--command", metavar="command",
        required=True, help="Command Line ."
        )

args = command.parse_args()
os.system(f'{args.command}')
print("\n")
