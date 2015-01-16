"""
David Schonberger
Project Euler - problem 74
Digit factorial chains
"""

import datetime
import math 

bef = datetime.datetime.now()
upper_start = 1000000
chain_len = 60
count = 0
for i in range(1, upper_start):
    res_set = set([i])
    s = sum( [math.factorial(int(ch)) for ch in str(i)])
    while(not s in res_set):
        res_set.add(s)
        s = sum( [math.factorial(int(ch)) for ch in str(s)])
    if(len(res_set) == chain_len):
        count += 1
    
aft = datetime.datetime.now()
print count, "chains of len = ", chain_len
print "\net:", aft - bef