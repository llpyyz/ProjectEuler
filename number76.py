"""
David Schonberger
Project Euler - problem 76
Counting summation [number theoretic partition function p(n)]
"""

import datetime
import math

def calc_pentagonal(k):
    return k * (3 * k - 1)/2

def find_k_range(n):
    r1 = (1 - math.sqrt(1+24*n))/6
    r2 = (1 + math.sqrt(1+24*n))/6
    return [int(math.ceil(r1)),int(math.floor(r2))]

def calc_k_set(lb, ub):
    return [x for x in range(lb, ub + 1) if x != 0]    

bef = datetime.datetime.now()
d = {0:1, 1:1, 2:2}
n = 10
for i in range(3,n+1):
    k_rng = find_k_range(i)
    k_set = calc_k_set(k_rng[0], k_rng[1])
    pn_set =  [(i - calc_pentagonal(x), int((-1)**(x-1))) for x in k_set]
    d[i] = sum([elt[1] * d[elt[0]] for elt in pn_set])
    
print d[n] - 1
aft = datetime.datetime.now()
print "\net:", aft - bef