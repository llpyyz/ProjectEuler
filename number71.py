"""
David Schonberger
Project Euler - problem 71
Ordered fractions
"""

import datetime
import math 


bef = datetime.datetime.now()
upper_denom = 10
min_dist = 1
res = [[math.ceil(3.0 * b / 7) - 1 , b, 3.0/7 - (math.ceil(3.0 * b / 7) - 1.0)/b] for b in range(1 , upper_denom + 1) ]
for elt in res:
    if(elt[2] < min_dist):
        min_dist = elt[2]
        min_num = elt[0]
        min_den = elt[1]
        
print res
print min_num, min_den, min_dist, "\n"
aft = datetime.datetime.now()
print "\net:", aft - bef