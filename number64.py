"""
David Schonberger
Project Euler - problem 64
Odd period square roots
"""

import math
import decimal
pr = 500
decimal.getcontext().prec = pr

def is_square(n):
    sq = False
    i = 1
    while(i**2 < n):
        i += 1
    if(i**2 == n):
        sq = True
    return sq
    
n = 10000
eps = decimal.Decimal(0.00000001)
odd_period_count = 0
for i in range(1,n + 1):
    if(not is_square(i)):
        done = False
        max_iters = 10000
        curr_iter = 1
        sq_n = decimal.Decimal(i).sqrt()
        a_0 = int(math.floor(decimal.Decimal(i).sqrt())) 
        x = sq_n - a_0
        cfrac = []
        period_len = 0
        while(curr_iter <= max_iters and not done):
            
            rx = decimal.Decimal(1.0)/decimal.Decimal(x)
            curr_diff = abs(rx - sq_n)
            curr_eps1 = abs(decimal.Decimal(curr_diff) - decimal.Decimal(math.floor(curr_diff)))
            curr_eps2 = abs(decimal.Decimal(curr_diff) - decimal.Decimal(math.ceil(curr_diff)))
            if(curr_eps1 <= eps or curr_eps2 <= eps):
                done = True
            
            x = rx - int(math.floor(rx))
            cfrac.append(int(math.floor(rx)))
            period_len += 1
            curr_iter += 1
        
        if(period_len % 2 == 1):
            odd_period_count += 1
            
print odd_period_count, "periods have odd length"
