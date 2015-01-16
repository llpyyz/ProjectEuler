"""
David Schonberger
Project Euler - problem 73
Counting proper fractions in a range
"""

import datetime

def gcd(a,b):
    while(b != 0):
        t = b
        b = a % b
        a = t
    return a

bef = datetime.datetime.now()
upper_denom = 12000
ub_num = 1
ub_den = 2
lb_num = 1
lb_den = 3
res1 = [[a,b] for b in range(2, upper_denom + 1) for a in range(1,b) if a*ub_den < b * ub_num and a*lb_den > b * lb_num]
res2 = [elt for elt in res1 if gcd(elt[0], elt[1]) == 1]


print "There are", len(res2), "proper fracs between:" 
print str(ub_num)+ "/"+str(ub_den), "and", str(lb_num)+ "/"+str(lb_den)
print "with denom <=", upper_denom
aft = datetime.datetime.now()
print "\net:", aft - bef