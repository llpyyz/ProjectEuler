"""
David Schonberger
Project Euler - problem 47
Distinct primes factors
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

def make_primes_list(n):
    prime_list = []
    for i in range(2,n+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

def get_prime_factorization(n):
    fac_list = []
    i = 2
    while(n > 1):
        count = 0
        while(n % i == 0):
            n = n / i
            count += 1
        if(count > 0):
            fac_list.append((i,count))
        i += 1
        
    return fac_list
    
upper = 150001
has_four_distinct_prime_factors = []

for i in range(2,upper):
    if(not is_prime(i)):
        fl = get_prime_factorization(i)
        if(len(fl) == 4):
            has_four_distinct_prime_factors.append(i)
        
for i in range(len(has_four_distinct_prime_factors) - 3):
    first = has_four_distinct_prime_factors[i]
    second = has_four_distinct_prime_factors[i+1]
    third = has_four_distinct_prime_factors[i+2]
    fourth = has_four_distinct_prime_factors[i+3]
    if(second - first == 1):
        if(third - second == 1):
            if(fourth - third == 1):
                print first, second, third, fourth
