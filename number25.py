"""
David Schonberger
Project Euler - problem #25

Find first term in Fibonacci sequence
with 1000 digits

"""
import math

n1 = 1
n2 = 1
num_digits = 1
bnd = 1000
idx = 2
while num_digits < bnd:
    tmp = n2
    n2 = n1+n2
    n1 = tmp
    num_digits = int(math.floor(math.log(n2,10) ) + 1) 
    idx += 1
    print "term", idx, "fn = ", n2, ";d = ",int(math.floor(math.log(n2,10) ) + 1), "\n" 
    
#gr = (1 + math.sqrt(5))/ 2.0
#num_digits = 0
#bnd = 10
#idx = 1
#while num_digits < bnd:
#    fnum = int(math.floor(gr ** idx / math.sqrt(5) + .5))
#    num_digits = int(math.floor(math.log(fnum,10) ) + 1) 
#    idx += 1
#
#print fnum
#print idx - 1,"\n"
