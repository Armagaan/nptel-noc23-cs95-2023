'''Script to read a table from the input file into a dictionary.'''

from argparse import ArgumentParser
from pprint import pprint

parser = ArgumentParser()
parser.add_argument("-i", "--input", required=True, type=str, help="input path")

args = parser.parse_args()

data = {}
with open(args.input, "r") as file_i:
    for i, line_i in enumerate(file_i.readlines()):
        if i % 2 == 0 or i == 1:
            continue
        # remove the newline and spaces
        __, alphabet, __, frequency, __, __, __ = line_i.rstrip().split()
        data[alphabet] = int(frequency)

pprint(data)
