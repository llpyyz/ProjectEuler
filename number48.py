"""
David Schonberger
Project Euler - problem 48
Self powers
"""
import datetime

bef = datetime.datetime.now()

def dec2bin(n):
    ret = []
    while(n > 0):
        ret.append(n % 2)
        n /= 2

    return ret

#compute x ^(2^p) mod 10 ^ m
def square_p_times_mod_10_to_m(x,p,m):
    if(p == 1):
        return (x ** 2) % (10 ** m)
    else:
        return square_p_times_mod_10_to_m((x**2) % (10 ** m), p - 1, m)

#return rightmost n digits of x**y
def n_digits_of_x_pow_y(x , y , n = 1):
    res = 1
    bin_rep = dec2bin(y)
    
    for i in range(len(bin_rep)):
        if(bin_rep[i] == 1):
            if(i == 0):
                res = x % (10 ** n)
            else:
                res = (res * square_p_times_mod_10_to_m(x,i,n)) % (10 ** n)    
                
    return res

upper = 100000
total = 0
dig = 10 #num of final digits to show
for i in range(1, upper+1):
    total = (total + n_digits_of_x_pow_y(i,i,dig)) % (10 ** dig)

print total
aft = datetime.datetime.now()
print "for sum of self powesr to", upper, "\net:",aft - bef
