'''Caeser cipher'''

import string
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-a", "--action", required=True, type=str, choices=["d", "e"],
                    help="Decrypt or Encrypt")
parser.add_argument("-i", "--input", required=True, type=str, help="input path")
parser.add_argument("-o", "--output", required=True, type=str, help="output path")
parser.add_argument("-k", "--key", required=True, type=int, help="key")

args = parser.parse_args()

KEY = args.key if args.action == "e" else - args.key
ALPHABETS = string.ascii_letters

def shift_alphabet(alphabet_, shift_):
    if alphabet_ not in ALPHABETS:
        return alphabet_
    index = ALPHABETS.index(alphabet_)
    new_index = (index + shift_) % len(ALPHABETS)
    return ALPHABETS[new_index]

with open(args.input, "r") as file_i, open(args.output, "w") as file_o:
    # ! This is suboptimal as it depends on the line size.
    for line_i in file_i.readlines():
        line_o = "".join(map(lambda alphabet: shift_alphabet(alphabet, KEY), line_i))
        file_o.write(line_o)

BUFFER_SIZE = 1 * 1024 # megabytes
with open(args.input, "r") as file_i, open(args.output, "w") as file_o:
    while True:
        # * This is indpendent of the line size.
        line_i = file_i.read(BUFFER_SIZE)
        if line_i == "":
            break
        line_o = "".join(map(lambda alphabet: shift_alphabet(alphabet, KEY), line_i))
        file_o.write(line_o)
