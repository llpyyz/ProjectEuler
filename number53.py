"""
David Schonberger
Project Euler - problem 53
Combinatoric selections
"""
import math

threshold = 1000000
upper_n = 100
count = 0
for n in range(1,upper_n + 1):
    for r in range(1,n):
        res1 = sum([math.log(i, 10) for i in range(2 , n + 1)])
        res2 = sum([math.log(i, 10) for i in range(2 , r + 1)])
        res3 = sum([math.log(i, 10) for i in range(2 , n - r + 1)])
        res = int(math.floor(res1 - res2 - res3)) + 1
        if(res >= 7):
            count += 1
    
print "For n not more than " , upper_n, "there are ***",count, "*** values of nCr that exceed", threshold
