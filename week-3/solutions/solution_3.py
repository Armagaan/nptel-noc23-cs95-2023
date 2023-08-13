# Remove duplicates from a list of integers retaining the right-most occurances.

import random
from time import time
from typing import List

random.seed(7)

def remove_duplicates(list_: List[int]) -> List[int]:
    '''Removes duplicates from a list while retaining the right-most occurances.'''
    # Make an empty list
    new_list_ = []
    # Iterate over the elements of the list in reverse order.
    for i in range(len(list_) - 1, -1, -1):
        # If the element is absent from the new list, append it to it's 0th position.
        element = list_[i]
        if element not in new_list_:
            new_list_ = [element] + new_list_
    return new_list_

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
    for __ in range(5_000):
        my_list.append(random.randint(0, 99))

    start = time()
    new_list = remove_duplicates(my_list)
    end = time()
    print(f"Len of list {len(my_list)}")
    print(f"Len of new list: {len(new_list)}")
    print(f"Elapsed time: {(end - start):.6f} seconds")
