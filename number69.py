"""
David Schonberger
Project Euler - problem 69
Totient maximum
"""

import datetime
import itertools
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
    
def gcd(a,b):
    while(b != 0):
        t = b
        b = a % b
        a = t
    return a
    
lower = 2*3*5*7
upper = 2*3*5*7
max_ratio = 1
max_n = 0
for i in range(lower , upper + 1):
    curr_phi = 0
    if(is_prime(i)):
        curr_ratio = 1.0*i/(i-1)
    else:
        for j in range(1,i):
            if(gcd(i,j) == 1):
                curr_phi += 1
                #print j
        curr_ratio = 1.0*i/curr_phi
        print curr_phi
    
    if(curr_ratio > max_ratio):
        max_n = i
        max_ratio = curr_ratio
        print max_n, max_ratio
        
        
print "\n\nfinal results:",max_n, max_ratio