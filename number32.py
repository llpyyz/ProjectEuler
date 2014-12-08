"""
David Schonberger
Project Euler - problem 32
Pandigital Products
"""
import itertools

def make_num(lst):
    num = 0
    for i in range(len(lst)):
        num += lst[i] * 10**(len(lst) -1 -i)
    
    return num
    
perm_lst =  list(itertools.permutations([1,2,3,4,5,6,7,8,9]))
prod_set = set([])
for t in perm_lst:
    for i in range(len(t) - 2):
        for j in range(i + 1, len(t) - 2):
            f1 = make_num(list(t[:i+1]))
            f2 = make_num(list(t[i+1:j+1]))
            prod = make_num(list(t[j+1:]))
            if(f1 * f2 == prod):
                prod_set.add(prod)

print sum(prod_set)