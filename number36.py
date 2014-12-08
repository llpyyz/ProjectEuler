"""
David Schonberger
Project Euler - problem 36
Double base palindromes
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

def dec_2_bin(n):
    ret = [] = []
    while(n > 0):
        ret.append(n % 2)
        n = n/2
    return ret
    
max_num = 1000000
num_sum = 0
for i in range(max_num):
    if(i % 2 == 1):
        bits = dec_2_bin(i)
        bits_copy = list(bits)
        bits_copy.reverse()
        digits = get_digits(i)
        digits_copy = list(digits)
        digits_copy.reverse()
        if bits == bits_copy and digits == digits_copy:
            num_sum += i
            
print num_sum
