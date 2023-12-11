import argparse

parser = argparse.ArgumentParser(
        description="CLI for print information ."
        )
parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="For Name !"
        )
parser.add_argument(
        "-a", "--age", metavar="age",
        required=True, help="For Age !"
        )
parser.add_argument(
        "-l", "--language", metavar="language",
        required=True, help="For Langauge !",
        choices=['en', 'sp']
        )

def language(name, age, lang):
    langs = {
        "en" : "hello",
        "sp" : "holla",
    }
    if name != "":
        print(f"{langs[lang]} {name} your {age}")
    else:
        print("You have to enter all information .")


args = parser.parse_args()
language(args.name, args.age, args.language)



