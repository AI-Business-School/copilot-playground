
def find_primes(max):
    sieve = [True] * (max + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(max ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max + 1, i):
                sieve[j] = False
    
    return [num for num, is_prime in enumerate(sieve) if is_prime]

print(find_primes(30))