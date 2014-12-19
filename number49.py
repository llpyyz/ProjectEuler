"""
David Schonberger
Project Euler - problem 49
Prime permutations
"""

import itertools
import math

def make_num(t):
    res = 0
    for i in range(len(t), 0, -1):
        res += t[len(t) - i] * (10 ** (i-1))
    return res

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

digits = [1,2,3,4,5,6,7,8,9]
four_combs = list(itertools.combinations_with_replacement(digits , 4))
prime_triples_list = []
for i in range(len(four_combs)):
    
    perms = list(itertools.permutations(four_combs[i]))
    primes_list = []
    for elt in perms:
        num = make_num(elt)
        if(is_prime(num)):
            primes_list.append(num)

    three_combs_of_primes = list(itertools.combinations(primes_list,3))
    true_count = 0
    for elt in three_combs_of_primes:
        if(elt[1] - elt[0] == elt[2] - elt[1] and elt[2] - elt[1] > 0):
            true_count += 1
            if(elt not in prime_triples_list):
                prime_triples_list.append(elt)
            
for elt in prime_triples_list:
    print "\nTuple of primes:\n",elt, "\nDiffs between consec terms:\n", elt[1] - elt[0], elt[2] - elt[1]
