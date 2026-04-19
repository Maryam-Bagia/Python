# Activity-7:

primes = [n for n in range(1, 51) if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))]
non_primes = [n for n in range(1, 51) if n not in primes]

print("Prime numbers:", primes)
print("Non-prime numbers:", non_primes)

# Output:
# Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# Non-prime numbers: [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50]




