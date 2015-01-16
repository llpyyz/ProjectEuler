"""
David Schonberger
Project Euler - problem 62
Cubic permutations
"""
import datetime
import math

def is_cube(n):
    i = 1
    ret = False
    while(i ** 3 <= n):
        if(i ** 3 == n):
            ret = True
            break
        i += 1
    return ret

def make_num_from_dig_lst(l):
    ret = 0
    for i in range(len(l)):
        ret += l[i] * (10 ** (len(l) - 1 - i))
    return ret

#given positive int n, returns range [a,b] such that x in [a,b] implies x**3 has n digits
def cubes_with_n_digits(n):
    a = int(math.ceil(10 ** (1.0*(n-1)/3 ) ))
    if(n % 3 == 0):
        b = int(math.floor(10 ** (1.0*(n)/3 ) ) - 1)
    else:
        b = int(math.floor(10 ** (1.0*(n)/3 ) ) )
    return [a,b]
    

bef = datetime.datetime.now()

num_digits = 3
exactly_five_perms = False
max_iters = 11
curr_iter = 1
while(not exactly_five_perms and curr_iter <= max_iters):
    r = cubes_with_n_digits(num_digits)
    cubes_lst = [x**3 for x in range(r[0],r[1] + 1)]
    digits_lists = []
    for cube in cubes_lst:
        ch_lst = [ch for ch in str(cube)]
        ch_lst.sort()
        dig_str = ''.join(ch_lst)
        digits_lists.append(dig_str)
            
    d = {}
    for i in range(len(digits_lists)):
        if(digits_lists[i] in d.keys()):
            d[digits_lists[i]].append(cubes_lst[i])
        else:
            d[digits_lists[i]] = [cubes_lst[i]]
                    
    mins_lst = []
    for val in d.values():
        if len(val) == 5:
            print "\n\nSuccess!!! Min cube:",min(val),"cubes list:\n", val
            mins_lst.append(min(val))
            print [int(x ** (1.0/3)) for x in val], "\n\n"
            exactly_five_perms = True
    
    num_digits += 1
    curr_iter += 1
    
print min(mins_lst)

aft = datetime.datetime.now()

print "et:", aft - bef
