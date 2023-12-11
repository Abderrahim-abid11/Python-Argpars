import argparse

calculator = argparse.ArgumentParser(
        description="Simple Calculator: -n1 3 -op + -n2"
        )
calculator.add_argument(
        "-n1", "--number1", metavar="number1",
        required=True, help="Number One ."
        )
calculator.add_argument(
        "-op", "--operator", metavar="operator",
        required=True, help='Use : + - x / %%',
        choices=['+','-','x','/','%']
        )
calculator.add_argument(
        "-n2", "--number2", metavar="number2",
        required=True, help="Number Two ."
        )

def calc(n1, op, n2):
    if op == '+':
        print(f"{n1} + {n2} = {float(n1)+float(n2)}")
    elif op == '-':
        print(f"{n1} - {n2} = {float(n1)-float(n2)}")
    elif op == 'x':
        print(f"{n1} x {n2} = {float(n1)*float(n2)}")
    elif op == '/':
        print(f"{n1} / {n2} = {float(n1)/float(n2)}")
    elif op == '%':
        print(f"{n1} % {n2} = {float(n1)%float(n2)}")
    else:
        print("Enter n1 and n2 and op(+-*/%)")

args = calculator.parse_args()
calc(args.number1, args.operator, args.number2)

