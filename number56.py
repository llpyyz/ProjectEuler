"""
David Schonberger
Project Euler - problem 56
Powerful digit sum
"""
print max(map(lambda s: sum([int(ch) for ch in s]), [str(a ** b) for a in range(1,100) for b in range(1, 100)]))
