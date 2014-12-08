"""
David Schonberger
Project Euler - problem 33
Digit cancelling fractions
"""
from operator import mul

#takes 2 digit number, returns list of digits
def get_digits(n):
    return [n/10,n%10]

#return list of comoon digits in two linput lists
def get_common_digits(l1,l2):
    rl = []
    for d in l1:
        if d in l2:
            rl.append(d)
    return rl

res = []
for num in range(10 , 99):
    for denom in range(num + 1 , 100):
        orig = 1.0 * num / denom
        num_digits = get_digits(num)
        denom_digits = get_digits(denom)
        cd = get_common_digits(num_digits, denom_digits)
        if(len(cd) == 1 and cd[0] > 0):
            num_digits.remove(cd[0])
            denom_digits.remove(cd[0])
            if(denom_digits[0] != 0):
                new = 1.0 * num_digits[0] / denom_digits[0]
                if(orig == new):
                    res.append(num_digits + denom_digits)
                

nums_prod = reduce(mul,[elt[0] for elt in res])
dens_prod = reduce(mul, [elt[1] for elt in res])
print "reduced denominator:\n", dens_prod / nums_prod