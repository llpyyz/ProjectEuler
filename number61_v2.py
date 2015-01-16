"""
David Schonberger
Project Euler - problem 61, revised
Cyclical figurate numbers
"""

def get_last_two_digits(n):
    return n % 100

def get_first_two_digits(n):
    return n / 100
    
def is_3rd_digit_0(n):
    return ((n/10) % 10) == 0
    
tn = [n*(n+1)/2 for n in range(1,160) if len(str(n*(n+1)/2)) == 4 and not is_3rd_digit_0(n*(n+1)/2)]
sn = [n**2 for n in range(1,160) if len(str(n**2)) == 4 and not is_3rd_digit_0(n**2)]
pn = [n*(3*n-1)/2 for n in range(1,160) if len(str(n*(3*n-1)/2)) == 4 and not is_3rd_digit_0(n*(3*n-1)/2)]
hx = [n*(2*n-1) for n in range(1,160) if len(str(n*(2*n-1))) == 4 and not is_3rd_digit_0(n*(2*n-1))]
hp = [n*(5*n-3)/2 for n in range(1,160) if len(str(n*(5*n-3)/2)) == 4 and not is_3rd_digit_0(n*(5*n-3)/2)]
on = [n*(3*n-2) for n in range(1,160) if len(str(n*(3*n-2))) == 4 and not is_3rd_digit_0(n*(3*n-2))]

i1 = 0
while(i1 < len(tn)):
    i2 = 0
    while(i2 < len(sn)):
        i3 = 0
        while(i3 < len(pn)):
            i4 = 0
            while(i4 < len(hx)):
                i5 = 0
                while(i5 < len(hp)):
                    i6 = 0
                    while(i6 < len(on)):
                        l = [tn[i1], sn[i2], pn[i3], hx[i4], hp[i5], on[i6]]
                        first_2_digits = [get_first_two_digits(n) for n in l]
                        last_2_digits = [get_last_two_digits(n) for n in l]
                        first_2_digits.sort()
                        last_2_digits.sort()
                        if(first_2_digits == last_2_digits):
                            print l, sum(l)
                        i6 += 1
                    i5 += 1
                i4 += 1
            i3 += 1
        i2 += 1
    i1 += 1
