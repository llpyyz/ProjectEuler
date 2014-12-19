"""
David Schonberger
Project Euler - problem 52
Permuted multiples
"""

def get_digits(n):
    return [ch for ch in str(n)]

the_range = range(100000,166666)
res = [[get_digits(x), get_digits(2*x), get_digits(3*x), get_digits(4*x), get_digits(5*x), get_digits(6*x)] for x in the_range]
for elt in res:
    for lst in elt:
        lst.sort()

i = 0
nums = []
for elt in res:
    res2 = []
    for elt2 in elt:
        res2.append(tuple(elt2))
    s = set(res2)
    if(len(s) == 1):
        if(the_range[i] not in nums):
            nums.append(the_range[i])
            print the_range[i], 2 * the_range[i], 3 * the_range[i], 4 * the_range[i], 5 * the_range[i], 6 * the_range[i]
    i += 1
