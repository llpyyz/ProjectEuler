"""
David Schonberger
Project Euler - problem 77
Prime summations [number theoretic partition function p(n)]
"""

import datetime
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
    
def calc_pentagonal(k):
    return k * (3 * k - 1)/2

def find_k_range(n):
    r1 = (1 - math.sqrt(1+24*n))/6
    r2 = (1 + math.sqrt(1+24*n))/6
    return [int(math.ceil(r1)),int(math.floor(r2))]

def calc_k_set(lb, ub):
    return [x for x in range(lb, ub + 1) if x != 0]    

def sort_list_tail(l):
    ret_lst = list(l)
    e = ret_lst.pop(0)
    ret_lst.sort()
    ret_lst = [e] + ret_lst
    return ret_lst
    
bef = datetime.datetime.now()

max_it = 100000
n = 10
base_list = [x for x in range(2,n - 1) if is_prime(x)]
bnd = 5000
done = False
mits = 1000000
cit = 0
while(not done and cit <= mits):
    l1 = [[base_list[j],base_list[i]] for i in range(len(base_list)) for j in range(i,len(base_list)) if base_list[j] + base_list[i] <= n and base_list[j] + base_list[i] != n - 1]
    curr_it = 0
    count = 0
    while(len(l1) > 0 and curr_it <= max_it):
        tmp = [x for x in l1 if sum(x) == n]
        count += len(tmp)
        l1 = [x for x in l1 if sum(x) < n]    
        l1 = [x + [y] for x in l1 for y in base_list if sum(x) + y <= n and sum(x) + y != n - 1]    
        s = set([])
        for elt in l1:
            elt.sort()
            s.add(tuple(elt))    
        l1 = [list(e) for e in s]
        curr_it += 1
        
    if(count > bnd):
        done = True
    else:
        n += 1
        idx = len(base_list) - 1
        base_list += [x for x in range(base_list[idx] + 1, n - 1) if is_prime(x)]
    cit += 1
    
print count, "partitions of", n , "in primes"

aft = datetime.datetime.now()
print "\net:", aft - bef
