"""
David Schonberger
Project Euler - problem 65
Convergents of e
"""

import math
import decimal
pr = 500
decimal.getcontext().prec = pr
    
num_convergents = 100
e = decimal.Decimal(1).exp()
curr_iter = 1
a_0 = decimal.Decimal(int(math.floor(e)))
x = e - a_0
cfrac = [int(a_0)] #init to whole number portion of e
curr_conv = [int(a_0),1]
prev_conv = [1,0]
while(curr_iter < num_convergents):
    
    rx = decimal.Decimal(1.0)/decimal.Decimal(x)
    x = rx - int(math.floor(rx))
    next_cf_term = int(math.floor(rx))
    cfrac.append(next_cf_term)
    tmp_conv = list(curr_conv)
    curr_conv = [next_cf_term * curr_conv[0] + prev_conv[0], next_cf_term * curr_conv[1] + prev_conv[1]]    
    prev_conv = list(tmp_conv)
    curr_iter += 1
            
print "sum of numerator digits for conv #",num_convergents, " = ",sum([int(ch) for ch in str(curr_conv[0])])
