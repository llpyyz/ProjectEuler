"""
David Schonberger
Project Euler - problem 39
Pandigital multiples
"""
upper = 100000
max_pandigital = 1

def is_pandigital(dig_str):
    ret = True
    for i in range(1,10):
        if not str(i) in dig_str:
            ret = False
            break
    return ret
    
for i in range(1,upper + 1):
    digit_str = ""
    j = 1
    too_big = False
    while len(digit_str) < 9 and not too_big:
        if len(digit_str) + len(str(i*j)) <= 9:
            digit_str += str(i*j)
            j += 1
        else:
            too_big = True
    if(is_pandigital(digit_str)):
        if int(digit_str) > max_pandigital:
            max_pandigital = int(digit_str)
            
print "max_pandigital:",max_pandigital
    
