"""
David Schonberger
Project Euler - problem 46
Goldbach's other conjecture
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

def make_odd_primes_list(n):
    prime_list = []
    for i in range(3,n+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list
    
def is_square(n):
    sq = False
    i = 1
    while(i**2 <= n and not sq):
        if(i**2 == n):
            sq = True
        else:
            i += 1
    return sq
    
max_odd = 9999
max_prime = 10000
prime_lst = make_odd_primes_list(max_prime)

print "\nAll odd composites under", max_odd, "that fail Goldbach's *other* conj:\n"
for i in range(9 , max_odd , 2):
    if(not is_prime(i)):
        sublist = [(i - x)/2 for x in prime_lst if x < i]
        goldbach_squares = [x for x in sublist if is_square(x)]
        if(len(goldbach_squares) == 0):
            print i

