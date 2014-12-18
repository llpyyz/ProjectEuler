"""
David Schonberger
Project Euler - problem 45
Triangular, Pentagonal, and Hexagonal numbers

"""
import datetime
import math
        
def is_odd_square(n):
    odd_sq = False
    i = 1
    while(i**2 <= n and not odd_sq):
        if(i**2 == n and i**2 % 2 == 1):
            odd_sq = True
        else:
            i += 1
    return odd_sq
    

bef = datetime.datetime.now()
#hn = 80000
pn = 10
tn = 30
tn_lst = []
pn_lst = []
#hn_lst = []

for i in range(1,tn):
    tn_lst.append(i*(i+1)/2)
    
for i in range(1,pn):
    pn_lst.append(i*(3*i-1)/2)

#for i in range(1,hn):
#    hn_lst.append(i*(2*i-1))
    
res1 = [(x,y) for x in tn_lst for y in pn_lst if x == y]
#res3 = [(x,y) for x in pn_lst for y in hn_lst if x == y]
aft = datetime.datetime.now()

print len(res1)
print "t_n that are p_n:",res1
print "et:", aft - bef


x = 1533776805
print (1 + math.sqrt(1 + 8 * x))/4 # = 27693 => 1533776805 is also a hexagonal #



