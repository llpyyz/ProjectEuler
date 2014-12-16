"""
David Schonberger
Project Euler - problem 40
Champernowne's constant
"""

s = ""
upper = 1000000
i = 1
while len(s) < upper:
    s += str(i)
    i += 1
    
print int(s[0]) * int(s[9]) *int( s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])