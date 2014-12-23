"""
David Schonberger
Project Euler - problem 55
Lychrel numbers
"""

upper = 10000
max_iters = 50

def reverse(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return n == reverse(n)

lychrel_count = 0
for i in range(1,upper):
    is_pal = False
    curr_iter = 0
    curr_val = i
    while(curr_iter < max_iters and not is_pal):
        curr_val += reverse(curr_val)
        if(is_palindrome(curr_val)):
            is_pal = True
        curr_iter += 1
    if(not is_pal):
        lychrel_count += 1

print "\n with a max iters of", max_iters, "there are", lychrel_count, "lychrel numbers under", upper