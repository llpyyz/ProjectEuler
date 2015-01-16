"""
David Schonberger
Project Euler - problem 60
Prime pair sets of size 5
"""
import math
import itertools

lower = 800000
upper = 900000

def is_prime(n):
    if n < 2:
        ret = False
    elif n == 2:
        ret = True
    else:
        ub = int(math.ceil(math.sqrt(n)))
        ret = True
        for i in range(2,ub + 1):
            if n % i == 0:
                ret = False
    return ret

def is_prime_concat(p1,p2):
    return is_prime(int(str(p1) + str(p2))) and  is_prime(int(str(p2) + str(p1)))

primes = [x for x in range(lower , upper) if is_prime(x)]
idx = 0
done = False
set_sum = 0
num_combos = 10
start_lst = [3 , 7 , 109 , 673]
while(idx < len(primes) and not done):
    combos_lst = list(itertools.combinations(start_lst + [primes[idx]] , 2))
    if(sum([is_prime_concat(elt[0], elt[1]) for elt in combos_lst]) == num_combos):
        done = True
        set_sum = sum(start_lst + [primes[idx]])
        print set_sum
        print start_lst + [primes[idx]]        
    idx += 1

print set_sum

###

"""
David Schonberger
Project Euler - problem 60
Prime pair sets of size 5
"""
import math
import itertools

def is_prime(n):
    if n < 2:
        ret = False
    elif n == 2:
        ret = True
    else:
        ub = int(math.ceil(math.sqrt(n)))
        ret = True
        for i in range(2,ub + 1):
            if n % i == 0:
                ret = False
    return ret

def is_prime_concat(p1,p2):
    return is_prime(int(str(p1) + str(p2))) and  is_prime(int(str(p2) + str(p1)))

lower = 3
upper = 30000
print "curr low and upper", lower, upper
primes = [x for x in range(lower , upper) if is_prime(x)]
print "searching a list of", len(primes), "primes, from", primes[0], "to", primes[len(primes) - 1], ":\n"

#set_sum = 0
main_sl = [3,7,109, 673]
#main_sl = [x for x in range(3,50) if is_prime(x)]

two_primes_combos = list(itertools.combinations(main_sl,2))
done = False
three_choose_two = 3
four_choose_two = 6
five_choose_two = 10

for i1 in range(len(two_primes_combos)):
    two_primes = list(two_primes_combos[i1])
    lower = max(two_primes) + 1
    i2 = 0
    while(i2 < len(primes) and not done):
        combos_lst_3c2 = list(itertools.combinations(two_primes + [primes[i2]] , 2))
        if(sum([is_prime_concat(elt[0], elt[1]) for elt in combos_lst_3c2]) == three_choose_two):
            three_primes = two_primes + [primes[i2]]
            i3 = 0
            while(i3 < len(primes) and not done):
                combos_lst_4c2 = list(itertools.combinations(three_primes + [primes[i3]] , 2))
                if(sum([is_prime_concat(elt[0], elt[1]) for elt in combos_lst_4c2]) == four_choose_two):
                    four_primes = three_primes + [primes[i3]]
                    i4 = 0
                    while(i4 < len(primes) and not done):
                        combos_lst_5c2 = list(itertools.combinations(four_primes + [primes[i4]] , 2))
                        if(sum([is_prime_concat(elt[0], elt[1]) for elt in combos_lst_5c2]) == five_choose_two):
                            print sum(four_primes + [primes[i4]]), four_primes + [primes[i4]]
                            done = True
                        i4 += 1
                i3 += 1
        i2 += 1
    if done:
        break
    
if not done:
    print "no result"
    
###

#print sl2_combos

#start_lst = [3,7, 2707, 94201]
#print start_lst, "\n"
#num_combos = 10
#i = 0
#while(i < len(primes)):
#    combos_lst = list(itertools.combinations(start_lst + [primes[i]] , 2))
#    if(sum([is_prime_concat(elt[0], elt[1]) for elt in combos_lst]) == num_combos):
#        set_sum = sum(start_lst + [primes[i]])
#        print set_sum, start_lst + [primes[i]]
#    i += 1
#


### results:
"""
used start_lst = [3 , 7 , 109 , 673]
added a fifth prime.
Tried all fifth primes <= 1,500,000 no result

Other lists of four, tested with fifth prime <= 100k:

[3,7,109]:
29178 [3, 7, 109, 29059] no res
79812 [3, 7, 109, 79693] no res
91278 [3, 7, 109, 91159] no res
93306 [3, 7, 109, 93187] no res

[3,7,673]:
23604 [3, 7, 673, 22921] no res
65976 [3, 7, 673, 65293] no res

[3,109,673]:
no sets of 4

[7,109,673]:
21676 [7, 109, 673, 20887] no res
35092 [7, 109, 673, 34303] no res

[3,7]:
239 [3, 7, 229]:
77058 [3, 7, 229, 76819] no res

551 [3, 7, 541]:
4710 [3, 7, 541, 4159] no res
74868 [3, 7, 541, 74317] no res
83574 [3, 7, 541, 83023] no res


833 [3, 7, 823]:
 28656 [3, 7, 823, 27823] no res

1247 [3, 7, 1237]:
78084 [3, 7, 1237, 76837] no res
95574 [3, 7, 1237, 94327] no res

2513 [3, 7, 2503]:
27702 [3, 7, 2503, 25189] no res
75576 [3, 7, 2503, 73063] no res
92712 [3, 7, 2503, 90199] no res

2717 [3, 7, 2707]:
96918 [3, 7, 2707, 94201]

4169 [3, 7, 4159]
4739 [3, 7, 4729]
5531 [3, 7, 5521]
9911 [3, 7, 9901]
10469 [3, 7, 10459]
10637 [3, 7, 10627]
14861 [3, 7, 14851]
15323 [3, 7, 15313]
19193 [3, 7, 19183]
19247 [3, 7, 19237]
20909 [3, 7, 20899]
21407 [3, 7, 21397]
22931 [3, 7, 22921]
24527 [3, 7, 24517]
24857 [3, 7, 24847]
25199 [3, 7, 25189]
27833 [3, 7, 27823]
29069 [3, 7, 29059]
29597 [3, 7, 29587]
29771 [3, 7, 29761]
29957 [3, 7, 29947]
34067 [3, 7, 34057]
38801 [3, 7, 38791]
41237 [3, 7, 41227]
41651 [3, 7, 41641]
48899 [3, 7, 48889]
51071 [3, 7, 51061]
51143 [3, 7, 51133]
54047 [3, 7, 54037]
54983 [3, 7, 54973]
55181 [3, 7, 55171]
56543 [3, 7, 56533]
58583 [3, 7, 58573]
60659 [3, 7, 60649]
61367 [3, 7, 61357]
61373 [3, 7, 61363]
61451 [3, 7, 61441]
61937 [3, 7, 61927]
62243 [3, 7, 62233]
65267 [3, 7, 65257]
65303 [3, 7, 65293]
71981 [3, 7, 71971]
73073 [3, 7, 73063]
74057 [3, 7, 74047]
74327 [3, 7, 74317]
76109 [3, 7, 76099]
76829 [3, 7, 76819]
76847 [3, 7, 76837]
77627 [3, 7, 77617]
79589 [3, 7, 79579]
79703 [3, 7, 79693]
80927 [3, 7, 80917]
82241 [3, 7, 82231]
83033 [3, 7, 83023]
84707 [3, 7, 84697]
90209 [3, 7, 90199]
91019 [3, 7, 91009]
91169 [3, 7, 91159]
93197 [3, 7, 93187]
94211 [3, 7, 94201]
94337 [3, 7, 94327]
96191 [3, 7, 96181]
97559 [3, 7, 97549]

"""
###
#idx1 = 0
#done = False
#if not done:
#    print "no result"
#
#while(idx1 < len(primes) and not done):
#    idx2 = idx1 + 1
#    while(idx2 < len(primes) and not done):
#        combos_lst = list(itertools.combinations(start_lst + [primes[idx1], primes[idx2]] , 2))
#        if(sum([is_prime_concat(elt[0], elt[1]) for elt in combos_lst]) == num_combos):
#            done = True
#            set_sum = sum(start_lst + [primes[idx1], primes[idx2]])
#            print set_sum
#            print start_lst + [primes[idx1], primes[idx2]]
#        idx2 += 1
#    idx1 += 1
#
#
#if done:
#    print start_lst + [primes[idx1-1], primes[idx2-1]], set_sum
#else:
#    print "no result"
