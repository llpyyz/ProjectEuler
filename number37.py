"""
David Schonberger
Project Euler - problem 37
Truncatble primes
"""
import math

#return list of digits in a number
def get_digits(n):
    size = int(math.floor(math.log(n,10))) + 1
    res = []
    for i in range(size):
        res.append(n % 10)
        n = n / 10
    return res

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

max_num =1000000
sum_of_trunc_primes = 0
count = 0
for i in range(11, max_num):
    if(is_prime(i)):
        trunc_primes = True
        l = int(math.floor(math.log(i,10))) + 1
        for j in range(1, l):
            trunc_primes = trunc_primes and is_prime(i % (10 ** j)) and is_prime(i / (10 ** j))
            if(not trunc_primes):
                break
        if(trunc_primes):
            sum_of_trunc_primes += i
            count += 1

print "\ncounted", count, "truncatable primes:"
print "\nsum of truncatble primes:\n",sum_of_trunc_primes
