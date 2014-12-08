"""
David Schonberger
Project Euler - problem #28
Number spiral diagonals

What is the sum of the diagonals of 
a 1001 by 1001 sprial?
"""

def num_spiral_diags_sum(n):
    s1 = 16*n*(n+1)*(2*n+1)/6 +2*n*(n+1) + 4*n
    return s1 + 1

spiral_size = 500
print num_spiral_diags_sum(spiral_size)
