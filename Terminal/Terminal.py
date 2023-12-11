import argparse
import pyfiglet

terminal = argparse.ArgumentParser(
        description="Terminal Dsiplay Name ."
        )
terminal.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="name"
        )

args = terminal.parse_args()
msg = pyfiglet.figlet_format(f"{args.name}", font="alphabet")
light_red = "\033[1;31m"
print("\n")
print(light_red, end="")
print(msg)
