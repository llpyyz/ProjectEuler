"""
David Schonberger
Project Euler - problem 72
Counting proper fractions
"""

import datetime
import operator

def get_prime_factorization_2(n):
    d = {}
    curr_divisor = 2
    while curr_divisor * curr_divisor <= n:
        while(n % curr_divisor == 0):
            if(curr_divisor in d.keys()):
                d[curr_divisor] += 1
            else:
                d[curr_divisor] = 1
            n /= curr_divisor
        if(curr_divisor == 2):
            curr_divisor += 1
        else:
            curr_divisor += 2
    if(n > 1):
        if(n in d.keys()):
            d[n] += 1
        else:
            d[n] = 1
    
    return d

def totient(n):
    pf_dict = get_prime_factorization_2(n)
    return reduce(operator.mul , [p ** i - p ** (i - 1) for p , i in pf_dict.items()] , 1)

bef = datetime.datetime.now()
upper_denom = 1000000
count = 0
for den in range(2,upper_denom + 1):
    count += totient(den)

print count
aft = datetime.datetime.now()
print "\net:", aft - bef, "\n\n"
