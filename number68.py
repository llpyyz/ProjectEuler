"""
David Schonberger
Project Euler - problem 68
Magic 5-gon ring
"""

import datetime
import itertools

def concat_list(l):
    res = [str(d) for d in l]
    return ''.join(res)

bef = datetime.datetime.now()

l = range(1,11)
combs_outer_ring = list(itertools.combinations(l,5))
max_16digit_str = 0
count = 0
for elt in combs_outer_ring:
    inner_ring = [x for x in l if x not in elt]
    perms_inner = list(itertools.permutations(inner_ring)) #120 perms
    last_4_outer = list(elt[1:])
    perms_last_4_outer = list(itertools.permutations(last_4_outer)) #24 perms
    
    for elt2 in perms_last_4_outer:
        if 10 in elt2:
            fl = True
            curr_outer = [elt[0]] + list(elt2)
            for elt3 in perms_inner:
                curr_inner = list(elt3) + [elt3[0]]
                sums = [curr_inner[i] + curr_inner[i+1] for i in range(0,5)]
                row_sums = [x+y for x,y in zip(sums,curr_outer)]
                s = set(row_sums)
                if(len(s) == 1):
                    ngon_rows = [[curr_outer[i], curr_inner[i], curr_inner[i+1]] for i in range(0,5)]
                    concat_rows = [concat_list(x) for x in ngon_rows]
                    j = int(''.join(concat_rows))
                    if(j > max_16digit_str):
                        max_16digit_str = j
        
print max_16digit_str
aft = datetime.datetime.now()
print "et:", aft - bef
