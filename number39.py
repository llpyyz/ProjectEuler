"""
David Schonberger
Project Euler - problem 39
Integer right triangles
"""
upper = 100
max_perim = 2000
pythag_triples = []
perims = {}
max_solns = 0

def gcd(n,m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)
    
for i in range(1 , upper):
    for j in range(i + 1 , upper):
        if gcd(i,j) == 1:
            x = j ** 2 - i ** 2
            y = 2 * i * j
            z = i** 2 + j ** 2
            if x + y + z <= max_perim:
                pythag_triples.append(set([x,y,z]))
                    
for elt in pythag_triples:
    curr_perim = sum(elt)
    i = 2
    while curr_perim < max_perim:
        tmp = set([i*e for e in elt])
        curr_perim = sum(tmp)
        if tmp not in pythag_triples and curr_perim < max_perim:                    
            pythag_triples.append(tmp)
        i += 1

for elt in pythag_triples:
    p = sum(elt)
    if p in perims.keys():
        perims[p] += 1
    else:
        perims[p] = 1

for k in perims.keys():
    if perims[k] > max_solns:
        max_solns = perims[k]
        max_solns_perim = k
        
print max_solns
print max_solns_perim
for elt in pythag_triples:
    if sum(elt) == max_solns_perim:
        print elt
