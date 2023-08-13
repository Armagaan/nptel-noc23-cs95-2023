# Compute the Sum of squares of the positives and the sum of cubes of the negatives in a list.

from typing import List

def split_sum(l: List[int]) -> List[int]:
    '''
    Compute the sum of squares of the positive numbers
    and the sum of cubes of the negatives in the input list
    '''
    pos, neg = 0, 0
    for i in l:
        if i > 0:
            pos += i ** 2
        else:
            neg += i ** 3
    return [pos, neg]

if __name__ == "__main__":
    print(split_sum([1, 3, -5]))
    print(split_sum([2, 4, 6]))
    print(split_sum([-19, -7, -6, 0]))
    print(split_sum([-1, 2, 3, -7]))
