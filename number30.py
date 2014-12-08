"""
David Schonberger
Project Euler - problem 30
Digit fifth powers
Find the sum of all the numbers 
that can be written as the sum of 
fifth powers of their digits.
"""
def get_digits(n):
    nstr = str(n)
    digits = []
    for d in nstr:
        digits.append(int(d))
    return digits

def get_sum_of_nth_pows(l,n):
    sum_of_digits = 0
    for d in l:
        sum_of_digits += d ** n
    return sum_of_digits

max_num = 10000000
num_sum = 0
power = 5
for i in range(2 , max_num + 1):
    dig_lst = get_digits(i)
    sum_of_pows_of_digits = get_sum_of_nth_pows(dig_lst, power)
    if(sum_of_pows_of_digits == i):
        num_sum += i
        print i
        
print "sum of numbers that can be written as sum of fifth powers of digits:\n",num_sum
