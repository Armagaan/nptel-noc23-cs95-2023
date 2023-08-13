# Repeat problem 3 using recursion.

import random
from sys import setrecursionlimit
from time import time
from typing import List

# Set according to need and only after you've confirmed your code's correctness.
setrecursionlimit(6_000)

def remove_duplicates(l: List[int]) -> List[int]:
    '''Removes duplicates from a list while retaining the right-most occurances.'''
    if len(l) <= 1:
        return(l)

    # If the first element re-occurs in the list, ignore it.
    if l[0] in l[1:]:
        return remove_duplicates(l[1:])
    else:
        return [l[0]] + remove_duplicates(l[1:])

if __name__ == "__main__":
    # Test cases.
    print(remove_duplicates([3, 1, 3, 5])) # [1, 3, 5]
    print(remove_duplicates([7, 3, -1, -5])) # [7, 3, -1, -5]
    print(remove_duplicates([3, 5, 7, 5, 3, 7, 10])) # [5, 3, 7, 10]

    # More test cases.
    print(remove_duplicates([5, 5, 5, 5, 1, 1, 5, 5, 5])) # [1, 5]
    print(remove_duplicates([8, 6, 4, 6, 8])) # [4, 6, 8]
    print(remove_duplicates([5])) # [5]
    print(remove_duplicates([])) # []

    # Time your code.
    my_list = []
    for __ in range(5_000): # for __ in range(100_000):
        my_list.append(random.randint(0, 99)) # my_list.append(random.randint(0, 9999))

    start = time()
    new_list = remove_duplicates(my_list)
    end = time()
    print(f"Len of list {len(my_list)}")
    print(f"Len of new list: {len(new_list)}")
    print(f"Elapsed time: {(end - start):.6f} seconds")
