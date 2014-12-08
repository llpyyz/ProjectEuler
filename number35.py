"""
David Schonberger
Project Euler - problem 35
Circular primes
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

#given a list, rotates the contents 1 space
def rotate(lst):
    tmp = list(lst)
    return [tmp.pop()] + tmp

#given a list of digits, returns
#the number they represent
#e.g [1,2,3] -> 123
def make_num(lst):
    num = 0
    for i in range(len(lst)):
        num += lst[i] * 10**(len(lst) - 1 - i)
    return num

#check if a number is prime
def is_prime(n):
    if n < 2:
        ret = False
    elif n == 2:
        ret = True
    else:
        ub = int(math.ceil(math.sqrt(n)))
        ret = True
        for i in range(2,ub + 1):
            if n % i == 0:
                ret = False
    return ret
    
max_num = 10000
cp_count = 0
for num in range(2 , max_num):
    prime_count = 0
    d = get_digits(num)
    for j in range(len(d)):
        d = rotate(d)
        if(is_prime(make_num(d))):
            prime_count += 1
    if(prime_count == len(d)):
        #print num
        cp_count += 1
        
print cp_count, "circular primes under", max_num
