"""
David Schonberger
Project Euler - problem 58
Spiral primes
"""
import math

def is_prime(n):
    if n < 2:
        ret = False
    elif n == 2:
        ret = True
    else:
        ub = int(math.ceil(math.sqrt(n)))
        ret = True
        for i in range(2,ub + 1):
            if n % i == 0:
                ret = False
    return ret

corner_lst = []
prime_percent = 1
i = 1
prime_count = 0
while(prime_percent >= 0.1):
    next_four = [4*(i**2) - 2*i + 1,  4*(i**2) + 1, 4*(i**2) + 2*i + 1, 4*(i**2) + 4*i + 1]
    new_primes = sum([is_prime(j) for j in next_four])
    prime_count += new_primes
    corner_lst += next_four
    prime_percent = 1.0 * prime_count / (4 * i + 1)
    i += 1

print "prime %",prime_percent,"side len:", 2*i - 1

