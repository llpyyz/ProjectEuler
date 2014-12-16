"""
David Schonberger
Project Euler - problem 41
Pandigital prime
"""
import math
import itertools

#check if a number is prime
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

def make_num(lst):
    s = ""
    for i in range(len(lst)):
        s += str(lst[i])
    
    return int(s)

l = [7,6,5,4,3,2,1]
not_prime = True
curr_perm = 0
while not_prime:
    num = make_num(list(itertools.islice(itertools.permutations(l),curr_perm, curr_perm + 1))[0])
    if(is_prime(num)):
        not_prime = False
        print num
    curr_perm += 1