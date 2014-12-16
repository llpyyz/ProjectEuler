"""
David Schonberger
Project Euler - problem 31
Coin sums
"""
c1 = 1
c1v = 200
c2 = 2
c2v = 100
c3 = 4
c3v = 50
c4 = 10
c4v = 20
c5 = 20
c5v = 10
c6 = 40
c6v = 5
c7 = 100
c7v = 2
c8 = 200
c8v = 1
count = 0
for i1 in range(c1 + 1):
    for i2 in range(c2 + 1):
        for i3 in range(c3 + 1):
            for i4 in range(c4 + 1):
                for i5 in range(c5 + 1):
                    for i6 in range(c6 + 1):
                        for i7 in range(c7 + 1):
                            for i8 in range(c8 + 1):
                                val = i1 * c1v + i2 * c2v + i3 * c3v + i4 * c4v + i5 * c5v + i6 * c6v + i7 * c7v + i8 * c8v 
                                if(val == 200):
                                    count += 1
                                                    
print "val == 200", count, "times"

