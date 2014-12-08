"""
David Schonberger
Project Euler - problem 34
Digit factorials
"""

import math

#return list of digits in a number
def get_digits(n):
    size = int(math.floor(math.log(n,10))) + 1
    res = []
    for i in range(size):
        res.append(n % 10)
        n = n / 10
    return res

max_val = 1000000
cuml_sum = 0
for i in range(3,max_val):
    digits = get_digits(i)
    
    fact_sum = 0
    for d in digits:
        fact_sum += math.factorial(d)
    if(i == fact_sum):
        cuml_sum += i
    
print cuml_sum
