from time import perf_counter

def print_combos_1(n, combo=[]):
    '''
    Print all combinations of numbers from 1 to n that sum up to n.
    Repetition is allowed. Permutations are allowed.
    '''
    for i in candidates:
        new_combo = combo + [i]
        # ! inefficient sum computation
        if sum(new_combo) == n:
            print(new_combo)
            return
        else:
            print_combos_1(n=n, combo=new_combo)

def print_combos_2(n, combo=[], combo_sum=0):
    '''
    Print all combinations of numbers from 1 to n that sum up to n.
    Repetition is allowed. Permutations are allowed.
    '''
    for i in candidates:
        new_combo = combo + [i]
        # * efficient sum computation
        new_combo_sum = combo_sum + i
        if new_combo_sum == n:
            print(new_combo)
            # Don't check rest of the candidates.
            return
        else:
            print_combos_2(n=n, combo=new_combo, combo_sum=new_combo_sum)

if __name__ == "__main__":
    N = 4
    candidates = range(1, N)

    start_time_1 = perf_counter()
    print_combos_1(n=N)
    end_time_1 = perf_counter()
    print(f"Time elapsed: {end_time_1 - start_time_1} seconds.")

    start_time_2 = perf_counter()
    print_combos_2(n=N)
    end_time_2 = perf_counter()
    print(f"Time elapsed: {end_time_2 - start_time_2} seconds.")
