'''
Read text from the input file and compute the character frequency into a dictionary.
Write this dictionary as a table in a text file. The cells are centered.
'''
import string
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-i", "--input", required=True, type=str, help="input filename")
parser.add_argument("-o", "--output", required=True, type=str, help="output filename")
args = parser.parse_args()

BUFFER_SIZE = 1 * 1024
ALPHABETS = string.ascii_lowercase
histogram = {alphabet: 0 for alphabet in ALPHABETS}
histogram["spl"] = 0

text_len = 0
with open(args.input, "r") as file:
    while True:
        line_in = file.read(BUFFER_SIZE).lower()
        # EOF
        if line_in == "":
            break
        # Remove newlines and spaces.
        line_in.replace("\n", "")
        line_in = "".join(line_in.split())
        # Update total text length.
        text_len += len(line_in)

        for letter in line_in.lower():
            if letter not in ALPHABETS:
                histogram["spl"] += 1
            else:
                histogram[letter] += 1

def table_line():
    return " " + "-" * (3 * col_width + 2) + "\n"

with open(args.output, "w") as file:
    col_width = 15
    file.write(table_line())
    file.write(
        f"|{'Alphabet'.center(col_width)}"
        f"|{'Frequency'.center(col_width)}|"
        f"{'Percentage'.center(col_width)}|\n"
    )
    file.write(table_line())
    for key, val in histogram.items():
        file.write(
            f"|{key.center(col_width)}"
            f"|{str(val).center(col_width)}|"
            f"{str(round(100 * val / text_len)).center(col_width)}|\n"
        )
        file.write(table_line())
