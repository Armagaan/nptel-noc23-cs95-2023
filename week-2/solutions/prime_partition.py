# Prime partition: Find primes that sum to number m.

def check_prime(m):
    if m == 1:
        return False
    for i in range(2, m // 2 + 1):
        if m % i == 0:
            return False
    return True

def find_primes_less_than(m):
    smaller_primes = []
    for i in range(2, m):
        if check_prime(i):
            smaller_primes.append(i)
    return smaller_primes

def prime_partition(m):
    if m < 1:
        print("Please enter a positive number.")
        return
    # find primes less than m
    smaller_primes = find_primes_less_than(m)

    # Select a prime
    for i in range(len(smaller_primes)):
        # Iterate over rest of the primes including itself.
        for j in range(i+1, len(smaller_primes)):
            # if sum == m:
            if smaller_primes[i] + smaller_primes[j] == m:
                print(f"Prime partition: {smaller_primes[i]} + {smaller_primes[j]} = {m}")
                return True
    return False

print(prime_partition(7))
print(prime_partition(185))
print(prime_partition(3432))
