"""
David Schonberger
Project Euler - problem 70
Totient permutation
"""

import datetime
import operator
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

#returns T or F according as a and b do/do not have same digits
def is_perm(a,b):
    digits_a = [ch for ch in str(a)]
    digits_a.sort()
    digits_b = [ch for ch in str(b)]
    digits_b.sort()
    return digits_a == digits_b


bef = datetime.datetime.now()
upper = 10000
min_ratio = 100
curr_min_totient_ratio_n = 0
for i in range(2, upper):
    totient_i = totient(i)
    if(is_perm(i, totient_i)):
        if(1.0 * i/totient_i < min_ratio):
            min_ratio = 1.0 * i/totient_i
            curr_min_totient_ratio_n = i

print "value <", upper,"that produces min perm totient ratio",curr_min_totient_ratio_n
print "min totient ratio", min_ratio

aft = datetime.datetime.now()
print "\net:", aft - bef