# Flip the input matrix in the desired direction.

from copy import deepcopy
from typing import List

def flip_matrix(matrix_: List[List[int]], direction: str) -> List[List[int]]:
    '''Return a flipped copy of the input matrix in the direction supplied by the user.'''
    # It is important to use deepcopy when copying nested lists.
    new_matrix_ = deepcopy(matrix_)

    if direction not in ["h", "v"]:
        return new_matrix_

    if direction == "h":
        for i in range(len(new_matrix_)):
            # Reverse row entries.
            new_matrix_[i].reverse()
    elif direction == "v":
        # Reverse entire rows.
        new_matrix_.reverse()
    return new_matrix_

def print_matrix(matrix_: List[List[int]]) -> None:
    '''Print the input matrix row wise.'''
    if len(matrix_) == 0:
        print("\n", [], "\n")
        return

    print()
    mat_len = len(matrix_)
    for i, row in enumerate(matrix_):
        print(row, end="")
        print("", end="" if i == mat_len - 1 else "\n")
    print()
    return

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(matrix)
    print_matrix(flip_matrix(matrix, "h"))
    print_matrix(flip_matrix(matrix, "v"))
    print_matrix(flip_matrix(flip_matrix(matrix, "h"), "v"))
    print_matrix(flip_matrix(flip_matrix(matrix, "v"), "h"))
    print_matrix(matrix)
