"""
David Schonberger
Project Euler - problem 50
Consecutive prime sum
"""
import math

upper = 10000
upper2 = 1000000
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

def is_odd_prime(n):
    if n <= 2:
        ret = False
    else:
        ub = int(math.ceil(math.sqrt(n)))
        ret = True
        for i in range(2,ub + 1):
            if n % i == 0:
                ret = False
    return ret

odd_primes = [x for x in range(3,upper+1) if is_odd_prime(x)]


res = [(j,sum(odd_primes[i:i+j])) for j in range(3, len(odd_primes) + 1,2) for i in range(len(odd_primes) - j + 1)]
res2 = [x for x in res if is_prime(x[1]) and x[1] <= upper2]

print res2, "\n"

#This is code to find primes that are sum of consecutive
#primes beginning with 2
#This shows that 958577 is formed by summming the first 536 primes.
#The next prime atfer that is 1005551 (bigger than 1MM) and formed 
#by summing the first 548 primes:

### begin ###

#primes = [x for x in range(2,upper+1) if is_prime(x)]
#sum_of_primes = []
#curr_sum = 0
#for i in range(len(primes)):
#    curr_sum += primes[i]
#    sum_of_primes.append((curr_sum, i+1))
#
#primes_in_sum_of_primes = [x for x in sum_of_primes if is_prime(x[0])]
#print primes_in_sum_of_primes, "\n"

### end ###