def sieve_of_eratosthenes(limit):
    # Create a boolean list "sieve" of size (limit+1) and initialize
    # all entries as True. A value in sieve[i] will finally be False
    # if i is not a prime, else True.
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for current_num in range(2, int(limit**0.5) + 1):
        if sieve[current_num]:
            # If sieve[current_num] is still True, then it is a prime number
            # Set all multiples of current_num as False since they can't be prime
            for multiple in range(current_num * current_num, limit + 1, current_num):
                sieve[multiple] = False

    # Compile the list of prime numbers
    prime_numbers = [num for num, is_prime in enumerate(sieve) if is_prime]

    return prime_numbers

if __name__ == "__main__":
    # limit = int(input("Enter the limit for prime number calculation: "))
    limit = 100000
    
    if limit < 2:
        print("There are no prime numbers in the specified range.")
    else:
        primes = sieve_of_eratosthenes(limit)
        print(f"Prime numbers up to {limit}: {primes}")

