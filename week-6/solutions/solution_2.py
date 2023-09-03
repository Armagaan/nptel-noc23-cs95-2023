from time import perf_counter

max_combo = []
combo_to_str = lambda combo: "-".join(str(i) for i in combo)

def first_combo_is_greater(c1, c2):
    '''
    Convert lists to strings and compare them lexicographically.
    Return True if c1 is greater than c2.
    '''
    c1 = combo_to_str(c1)
    c2 = combo_to_str(c2)
    return c1 > c2

def print_combos(n, combo=[], combo_sum=0):
    '''
    Print all combinations of numbers from 1 to n that sum up to n.
    Repetition is allowed. Permutations are not allowed.
    '''
    # Since every child function called during recursion will assign some value to max_combo,
    # we need to inform them to use the global value max_combo
    # rather than using max_combo as a local variable
    global max_combo

    for i in candidates:
        new_combo = combo + [i]
        new_combo_sum = combo_sum + i
        # Convert combo to string and compare with the largest one we've seen so far.
        if new_combo_sum == n:
            # Sorting is important to find duplicate combos.
            new_combo.sort()
            # We see combos in increasing lexicographic order due the way we traverse the tree.
            # Therefore, if new_combo is lexicographically smaller than max_combo,
            # we must've seen it before.
            if first_combo_is_greater(c1=new_combo, c2=max_combo):
                print(new_combo)
                max_combo = new_combo
            # Don't check rest of the candidates.
            # * Note
            # The return statement is outside the if-clause.
            # If it is placed inside the if-clause,
            # the function will continue to check other candidates of the for-loop.
            return
        else:
            print_combos(n=n, combo=new_combo, combo_sum=new_combo_sum)

if __name__ == "__main__":
    N = 4
    candidates = range(1, N)

    start_time = perf_counter()
    print_combos(n=N)
    end_time = perf_counter()
    print(f"Time elapsed: {end_time - start_time} seconds.")
