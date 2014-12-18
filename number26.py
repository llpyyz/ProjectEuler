"""
David Schonberger
Project Euler - problem 26
Reciprocal cycles
"""
import decimal
pr = 3000
decimal.getcontext().prec = pr
n = 1000
remove = 20
max_cycle_len = 0

def get_recip_str(n):
    return str(decimal.Decimal(1) / decimal.Decimal(n))

for j in range(1,1000):
    num_str = get_recip_str(j)
    num_str_ch = num_str[remove:]
    if(len(num_str_ch) > 0):
        for i in range(2,n):
            subs = num_str_ch[ : i]
            nextsubs = num_str_ch[i : 2*i]
            ac = num_str_ch.count(subs)
            ec = len(num_str_ch)/len(subs)
            if(subs == nextsubs and abs(ec - ac) <= 1):
                cycle_len = len(subs)
                if(cycle_len > max_cycle_len):
                    max_cycle_len = cycle_len
                    denom = j
                break

print "\n\nmax cycle len = ",max_cycle_len
print "corresponding denom", denom
