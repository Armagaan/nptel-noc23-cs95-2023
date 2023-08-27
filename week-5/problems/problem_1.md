# Caeser Cipher

Caesar cipher is a simple encryption technique that was developed by Julius Caesar. It is a type of substitution cipher, where each letter in the plaintext is replaced by a letter that is a fixed number of positions down the alphabet. For example, if the shift is 3, then A would be replaced by D, b would be replaced by e, and so on.

To encrypt a message using a Caesar cipher, you first need to choose a shift value. Once you have chosen a shift value, you then need to replace each letter in the plaintext with the letter that is that many positions down the alphabet.

For example, if the shift value is 3, then the plaintext message "hello" would be encrypted as "khoor"; "zoo" would be encrypted as "crr".

To decrypt a message that has been encrypted using a Caesar cipher, you simply need to reverse the encryption process. In other words, you replace each letter in the ciphertext with the letter that is that many positions up the alphabet.

For example, the ciphertext message "khoor" would be decrypted as "hello" if the shift value was 3.

---

Implement Caeser cipher.
- Your script should take the following inputs: `action (encrypt or decrypt)`, `input_file_path`, `output_file_path`, `shift` and store the output at the `output_file_path`.
- Your algorithm should be case sensitive.
- It should leave non-alphabetic characters as is.
- It should preserve spaces and newlines.

Here's the code for accepting the user input:
```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-a", "--action", required=True, type=str, choices=["d", "e"],
                    help="Decrypt or Encrypt")
parser.add_argument("-i", "--input", required=True, type=str, help="input path")
parser.add_argument("-o", "--output", required=True, type=str, help="output path")
parser.add_argument("-k", "--key", required=True, type=int, help="key")

args = parser.parse_args()
input_path = args.input
...
```

If you're encrypting with shift=5, you'll run your program as follows:
```bash
# long form
python caeser.py --action e --input file_i.txt --output file_o.txt --key 5
# short form
python caeser.py -a e -i file_i.txt -o file_o.txt -k 5
```