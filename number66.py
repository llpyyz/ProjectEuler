"""
David Schonberger
Project Euler - problem 66
Minimal Solution to Pell's equation
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

#computes cfrac of irrational sqrt(n), i.e. n not a perfect square
def get_cfrac_sqrt_n(n , eps, m):
    done = False
    max_its = m
    curr_iter = 1
    sq_n = decimal.Decimal(n).sqrt()
    a_0 = int(math.floor(decimal.Decimal(n).sqrt())) 
    x = sq_n - a_0
    cfrac = [int(a_0)]
    while(curr_iter <= max_its and not done):            
        rx = decimal.Decimal(1.0)/decimal.Decimal(x)
        curr_diff = abs(rx - sq_n)
        
        curr_eps1 = abs(decimal.Decimal(curr_diff) - decimal.Decimal(math.floor(curr_diff)))
        curr_eps2 = abs(decimal.Decimal(curr_diff) - decimal.Decimal(math.ceil(curr_diff)))
        if(curr_eps1 <= eps or curr_eps2 <= eps):
            done = True
        
        x = rx - int(math.floor(rx))
        cfrac.append(int(math.floor(rx)))
        curr_iter += 1
        
    if(curr_iter > max_its):
        print "Error. Period of this cfrac exceeds the max iters you passed in."
        print "Call the function again with larger max iters."
        return []
    else:
        return cfrac

def calc_nth_convergent(cf, n):    
    curr_conv = [int(cf[0]),1]
    prev_conv = [1,0]
    curr_iter = 1
    while(curr_iter < n):
        tmp_conv = list(curr_conv)
        curr_conv = [cf[curr_iter] * curr_conv[0] + prev_conv[0], cf[curr_iter] * curr_conv[1] + prev_conv[1]]    
        prev_conv = list(tmp_conv)
        
        curr_iter += 1
      
    return curr_conv

#odd len period cfrac extended to have
#sufficient terms to solve Pell's
def expand_odd_len_cf(cf):
    cf_tmp = list(cf)
    cf_tmp.pop(0)
    cf_tmp = 2 * cf_tmp
    cf_tmp.pop()
    cf_tmp  = [cf[0]] + cf_tmp
    return cf_tmp


n = 1000
eps = decimal.Decimal(0.00000001)
max_iters = 10000
max_x = 0
max_D = 0
for i in range(1,n + 1):
    if(not is_square(i)):
        cfrac = get_cfrac_sqrt_n(i,eps, max_iters)
        period_len = len(cfrac) - 1
        #print cfrac
        if(period_len % 2 == 1):
            num_convergents = 2 * period_len
            cfrac = expand_odd_len_cf(cfrac)
        else:
            num_convergents = period_len
            
            
        conv = calc_nth_convergent(cfrac,num_convergents)
        if(conv[0] > max_x):
            max_x = conv[0]
            max_D = i
        #print "minimal soln to pell's eqn:", i, conv[0], conv[1], conv[0] ** 2 - i * conv[1] ** 2
            
print "D for minimal solns to pell's where x is largest is: ", max_D
print "max x :", max_x
