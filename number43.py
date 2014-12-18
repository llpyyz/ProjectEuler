"""
David Schonberger
Project Euler - problem 43
Pandigital Sub-string divisibility
"""
import itertools

def make_num(lst):
    s = ""
    for i in range(len(lst)):
        s += str(lst[i])
    
    return int(s)

l = ['0','1','2','3','4','5','6','7','8','9']
prime_lst = [2,3,5,7,11,13,17]
cumul_sum = 0
count = 0
res = list(itertools.permutations(l))
last_idx = len(l) - 2
for elt in res:
    div_by_primes = True
    for j in range(1,last_idx):
        if(make_num(elt[j : j + 3]) % prime_lst[j-1] != 0):
            div_by_primes = False
        if(not div_by_primes):
            break
    if(div_by_primes):
        cumul_sum += make_num(elt)
        count += 1

print "\ncount:",count
print "\npandigital num sum:", cumul_sum
