"""
David Schonberger
Project Euler - problem 63
Powerful digit counts
"""

import datetime
import math

def kth_pow_with_n_digits(n,k):
    ret = []
    a = int(math.ceil(10 ** (1.0*(n-1)/k ) ))
    if(n % k == 0):
        b = int(math.floor(10 ** (1.0*(n)/k ) ) - 1)
    else:
        b = int(math.floor(10 ** (1.0*(n)/k ) ) )
    if a < b:
        ret = [a,b]
    elif(a == b):        
        ret  = [a]
    return ret
    
bef = datetime.datetime.now()
num_digits = 1
count = 0
max_iters = 50
curr_iter = 1
while(curr_iter <= max_iters):
    res = kth_pow_with_n_digits(num_digits, num_digits)
    print "num digits/power:",num_digits, "results:", res, "\n"
    if(len(res) == 1):
        count += 1
    elif(len(res) > 1):
        count += res[1] - res[0] + 1
    num_digits += 1
    curr_iter += 1

print count    
aft = datetime.datetime.now()
print "et:", aft - bef
