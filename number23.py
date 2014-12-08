"""
David Schonberger
Project Euler - problem #23
Sum of Non-abundants

A perfect number is a number for which the sum of its proper 
divisors is exactly equal to the number. For example, 
the sum of the proper divisors of 28 would be 
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper 
divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant 
numbers is 24. By mathematical analysis, it can be shown that 
all integers greater than 28123 can be written as the sum of two 
abundant numbers. However, this upper limit cannot be reduced 
any further by analysis even though it is known that the greatest 
number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot 
be written as the sum of two abundant numbers.

Solved : 11/30/2014
"""

n = 28123
#make list of abundant numbers
abundant_num_lst = []
for i in range(2 , n + 1):
    div_sum = 0
    for j in range(1 , i/2 + 1):
        if i % j == 0:
            div_sum += j
    if div_sum > i:
        abundant_num_lst.append(i)
        
sum_of_2_abundants_2 = set([])
for i in range(len(abundant_num_lst)):
    for j in range(i, len(abundant_num_lst)):
        s = abundant_num_lst[i] + abundant_num_lst[j]
        if s <= n:
            sum_of_2_abundants_2.add(s)

lst = list(sum_of_2_abundants_2)
lst.sort()

sum_nonabundants = 0
for i in range(1, n + 1):
    if not i in lst:
        sum_nonabundants += i

print sum_nonabundants #4179871

#largst number < 28123 that is not the sum
#of two adundants
for i in range(n,1,-1):
    if not i in lst:
        print i #20161
        break
