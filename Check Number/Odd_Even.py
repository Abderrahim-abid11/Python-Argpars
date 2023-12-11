import argparse

check = argparse.ArgumentParser(
        description = "Check Number if odd or even ."
        )
check.add_argument(
        "-n", "--number", metavar="number",
        required=True, help="Enter Number ."
        )

def check_number(number):
    if int(number) % 2 == 0:
        print(f"{number} is Even Number .")
    else:
        print(f"{number} is Odd Number .")

args = check.parse_args()
check_number(args.number)
