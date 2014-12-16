"""
David Schonberger
Project Euler - problem 43
Pandigital Sub-string divisibility
"""
import math
import itertools

def make_num(lst):
    s = ""
    for i in range(len(lst)):
        s += str(lst[i])
    
    return int(s)


l = ['0','1','2','3','4','5','6','7','8','9']
upper = math.factorial(len(l))
prime_lst = [2,3,5,7,11,13,17]
cumul_sum = 0
count = 0
for i in range(upper):
    next_perm = list(itertools.islice(itertools.permutations(l), i, i + 1))[0]
    div_by_primes = True
    for j in range(1,8):
        if(make_num(next_perm[j : j + 3]) % prime_lst[j-1] != 0):
            div_by_primes = False
        if(not div_by_primes):
            break
    if(div_by_primes):
        print "perm satisfies div property:", next_perm, "num:",make_num(next_perm)
        cumul_sum += make_num(next_perm)
        count += 1

print "count:",count
print "pandigital num sum:", cumul_sum