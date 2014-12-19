"""
David Schonberger
Project Euler - problem 51
Prime digit replacements
"""
import math
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

def make_num(lst):
    num = 0
    for i in range(len(lst)):
        num += lst[i] * 10 ** (len(lst) - 1 - i)
    return num

#Do not replace the last digit. 
#Fix 0 or more of other digits the replace others
last_digits = [1,3,7,9]
first_digits = [1,2,3,4,5,6,7,8,9]
digits = [0,1,2,3,4,5,6,7,8,9]
fd_idx = 0
while(fd_idx < len(first_digits)):
    ld_idx = 0
    while(ld_idx < len(last_digits)):
                    
        ########################        
        ### begin code chunk ###
        ########################        
        #six digit numbers
        #replace first digit plus two of digits 2-5; fix the other two
        #
        for d1 in range(len(digits)):
            for d2 in range(len(digits)):
                res1 = [make_num([i, digits[d1], digits[d2],i,i, last_digits[ld_idx]]) for i in first_digits]
                res2 = [make_num([i, digits[d1], i, digits[d2],i, last_digits[ld_idx]]) for i in first_digits]
                res3 = [make_num([i, digits[d1], i, i, digits[d2], last_digits[ld_idx]]) for i in first_digits]
                res4 = [make_num([i, i, digits[d1], digits[d2],i, last_digits[ld_idx]]) for i in first_digits]
                res5 = [make_num([i, i, digits[d1], i, digits[d2], last_digits[ld_idx]]) for i in first_digits]
                res6 = [make_num([i, i,i, digits[d1], digits[d2], last_digits[ld_idx]]) for i in first_digits]
                prime_count1 = len([x for x in res1 if is_prime(x)])
                prime_count2 = len([x for x in res2 if is_prime(x)])
                prime_count3 = len([x for x in res3 if is_prime(x)])
                prime_count4 = len([x for x in res4 if is_prime(x)])
                prime_count5 = len([x for x in res5 if is_prime(x)])
                prime_count6 = len([x for x in res6 if is_prime(x)])
                if(prime_count1 > 7):
                    print res1
                if(prime_count2 > 7):
                    print res2
                if(prime_count3 > 7):
                    print res3
                if(prime_count4 > 7):
                    print res4    
                if(prime_count5 > 7):
                    print res5    
                if(prime_count6 > 7):
                    print res6    
        
        ### end of code chunk ####
                    
        ld_idx += 1
    fd_idx += 1

#[121313, 222323, 323333, 424343, 525353, 626363, 727373, 828383, 929393]

#### gallery of old codes:

        #six digit numbers    
        #case 2: fix three digits, chg other one (4 main combos)
#        for d1 in range(len(digits)):
#            for d2 in range(len(digits)):
#                for d3 in range(len(digits)):
#                    res1 = [make_num([first_digits[fd_idx], digits[d1], digits[d2],digits[d3],i, last_digits[ld_idx]]) for i in digits]
#                    res2 = [make_num([first_digits[fd_idx], digits[d1], digits[d2],i, digits[d3], last_digits[ld_idx]]) for i in digits]
#                    res3 = [make_num([first_digits[fd_idx], digits[d1], i, digits[d2], digits[d3], last_digits[ld_idx]]) for i in digits]
#                    res4 = [make_num([first_digits[fd_idx], i, digits[d1], digits[d2], digits[d3], last_digits[ld_idx]]) for i in digits]
#                    prime_count1 = len([x for x in res1 if is_prime(x)])
#                    prime_count2 = len([x for x in res2 if is_prime(x)])
#                    prime_count3 = len([x for x in res3 if is_prime(x)])
#                    prime_count4 = len([x for x in res4 if is_prime(x)])
#                    if(prime_count1 > 7):
#                        print res1
#                    if(prime_count2 > 7):
#                        print res2
#                    if(prime_count3 > 7):
#                        print res3
#                    if(prime_count4 > 7):
#                        print res4    

###
#            #####no results#####
#            res1 = [make_num([first_digits[fd_idx], digits[fixed_dig_idx], digits[fixed_dig_idx],i,i, last_digits[ld_idx]]) for i in digits]
#            res2 = [make_num([first_digits[fd_idx], digits[fixed_dig_idx], i, digits[fixed_dig_idx],i, last_digits[ld_idx]]) for i in digits]
#            res3 = [make_num([first_digits[fd_idx], digits[fixed_dig_idx], i,i, digits[fixed_dig_idx], last_digits[ld_idx]]) for i in digits]
#            res4 = [make_num([first_digits[fd_idx], i, digits[fixed_dig_idx], digits[fixed_dig_idx],i, last_digits[ld_idx]]) for i in digits]
#            res5 = [make_num([first_digits[fd_idx], i, digits[fixed_dig_idx], i, digits[fixed_dig_idx], last_digits[ld_idx]]) for i in digits]
#            res6 = [make_num([first_digits[fd_idx], i,i,digits[fixed_dig_idx], digits[fixed_dig_idx], last_digits[ld_idx]]) for i in digits]            
#            prime_count1 = len([x for x in res1 if is_prime(x)])
#            prime_count2 = len([x for x in res2 if is_prime(x)])
#            prime_count3 = len([x for x in res3 if is_prime(x)])
#            prime_count4 = len([x for x in res4 if is_prime(x)])
#            prime_count5 = len([x for x in res5 if is_prime(x)])
#            prime_count6 = len([x for x in res6 if is_prime(x)])

###

#        five digit numbers:
#        fix one digit, chg the other two  
#        [56003, 56113, 56223, 56333, 56443, 56553, 56663, 56773, 56883, 56993]
#        res1 = [make_num([first_digits[fd_idx], digits[fixed_dig_idx], i, i, last_digits[ld_idx]]) for i in digits ]
#        res2 = [make_num([first_digits[fd_idx], i, digits[fixed_dig_idx], i, last_digits[ld_idx]]) for i in digits ]
#        res3 = [make_num([first_digits[fd_idx], i, i, digits[fixed_dig_idx], last_digits[ld_idx]]) for i in digits ]
            
        ### ###            
        #five digit numbers, digit replace on all three middle digits
        #NO RESULTS
#        res = [make_num([first_digits[fd_idx], i, i, i, last_digits[ld_idx]]) for i in digits ]            
#        print [x for x in res if is_prime(x)]
#        pc = len([x for x in res if is_prime(x)])
#        if(pc > 7):
#            print "***\nFound >= 8:",res, "\n***"
        ### ###

###

        ######################
        ###begin code chunk###
        ######################
        #five digit numbers:
        #allow replacment of first digit
        #fix one, replace other three, but now 0 is not allowed as replacement
        #NO RESULTS
#        fixed_digit_idx = 0
#        while(fixed_digit_idx < len(digits)):
#            res = [make_num([i, i, i, digits[fixed_digit_idx],  last_digits[ld_idx]]) for i in first_digits ]
#                    
#            pc = len([x for x in res if is_prime(x)])
#            if(pc > 7):
#                print "***\nFound >= 8:",res, "\n***"
#            fixed_digit_idx += 1
            
        ###end code chunk###

###

        ######################    
        ###begin code chunk###
        ######################            
        #six digit numbers
        #replacement of all first five digits
        #NO RESULTS            
#        res = [make_num([i, i, i, i,i,  last_digits[ld_idx]]) for i in first_digits ]    
#        pc = len([x for x in res if is_prime(x)])
#        if(pc > 7):
#            print "***\nFound >= 8:",res, "\n***"
                
        ###end code chunk###

###
            #six digit numbers:
            #Case 1a: rplacement on middle four
            #fix one digit, chg the other three (4 combos)
            #NO RESULTS
#            res1 = [make_num([first_digits[fd_idx], digits[fixed_dig_idx], i,i,i, last_digits[ld_idx]]) for i in digits]
#            res2 = [make_num([first_digits[fd_idx], i, digits[fixed_dig_idx], i,i, last_digits[ld_idx]]) for i in digits]
#            res3 = [make_num([first_digits[fd_idx], i, i, digits[fixed_dig_idx], i, last_digits[ld_idx]]) for i in digits]
#            res4 = [make_num([first_digits[fd_idx], i, i,i, digits[fixed_dig_idx], last_digits[ld_idx]]) for i in digits]
#            prime_count1 = len([x for x in res1 if is_prime(x)])
#            prime_count2 = len([x for x in res2 if is_prime(x)])
#            prime_count3 = len([x for x in res3 if is_prime(x)])
#            prime_count4 = len([x for x in res4 if is_prime(x)])
