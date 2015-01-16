"""
David Schonberger
Project Euler - problem 75
Singular integer right triangles
"""

import datetime
import math 

def gcd(a,b):
    while(b != 0):
        t = b
        b = a % b
        a = t
    return a


bef = datetime.datetime.now()
upper_len = 1500000
max_s = 1000
triples = [[2*s*t , s**2 - t**2, s**2 + t**2] for s in range(2,max_s) for t in range(1,s) if gcd(s,t) == 1 and (s - t)%2 == 1 and 2*s*t + 2*s**2 <= upper_len]
d = {}
for elt in triples:
    s = sum(elt)
    if(not s in d.keys()):
        d[s] = 1
        mult = 2
        while(mult * s <= upper_len):
            if(mult * s not in d.keys()):
                d[mult * s] = 1
            else:
                d[mult * s] += 1
            mult += 1
    else:
        d[s] += 1
        mult = 2
        while(mult * s <= upper_len):
            if(mult * s not in d.keys()):
                d[mult * s] = 1
            else:
                d[mult * s] += 1
            mult += 1

#print triples, "\n\n"
#print d, "\n\n"
res = [k for k,v in d.items() if v == 1]
#print res, "\n\n"
print len(res)
aft = datetime.datetime.now()
print "\net:", aft - bef