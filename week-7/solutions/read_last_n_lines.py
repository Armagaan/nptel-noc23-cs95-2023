import os

def read_last_n_lines(filepath, N):
    newlines_seen = 0
    with open(filepath, "rb") as file:
        try:
            # Go the the last character.
            file.seek(-1, os.SEEK_END)
            # Enter an infinite loop.
            while True:
                char = file.read(1)
                # If it is not a newline character:
                if char != b'\n':
                    # Go two characters back as we've read 1 character
                    file.seek(-2, os.SEEK_CUR)
                else:
                # If it is a newline character:
                    # increment the counter.
                    newlines_seen += 1
                    # check counter against N + 1 as the \n characters are at the end of each line.
                    if newlines_seen == N + 1:
                        break
                    else:
                        file.seek(-2, os.SEEK_CUR)
                        # Go two characters back as we've read 1 character.
        except OSError:
            # read start
            file.seek(0)
        
        lines = file.readlines()
        lines = [line.decode().strip() for line in lines]
        return lines

if __name__ == "__main__":
    transactions = read_last_n_lines("log/0.log", 3)
    for i in transactions:
        print(i)
