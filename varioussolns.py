"""
Project Euler
Author: David Schonberger
Created: 10/4/2014
"""
import math

###########################################################
#Problem 1 - Find sum of all multiples of 3 or 5 below 1000
###########################################################
def sum_multiples(upperbnd):
    """
    Problem 1: Find sum of all multiples of 3 or 5 below upperbnd
    """
    total = 0
    for count in range(1 , upperbnd):
        if(count % 3 == 0 or count % 5 == 0):
            total += count
    return total
    
n = 1000
print "sum of multiple of 3 or 5 under ", n, "is", sum_multiples(n)


#####


#####################################################################
#Problem 2 - Find sum of all even terms from Fibonacci seq with terms 
#not exceeding a given upper bnd
#####################################################################

def sum_even_fibonacci(upperbnd):
    """
    Problem 2: sum of all even fibonacci <= 4000000
    """
    fib1 = 1
    fib2 = 2
    fib_sum = 2
    fib = fib1 + fib2
    while(fib <= upperbnd):
        if fib % 2 == 0:
            fib_sum += fib
        fib1 = fib2
        fib2 = fib
        fib = fib1 + fib2
    return fib_sum

n = 4000000
ret = sum_even_fibonacci(n)
print "sum of even fibonacci numbers <= ", n, "is", ret


#####


###################################################
#Problem 3 - largest prime factor of a given number
###################################################

def find_largest_prime_factor(number):
    copy_of_num = number
    upperbnd = int(math.ceil(math.sqrt(number)))
    largest_factor = 2
    while number > 1:
        while (number % largest_factor == 0):
            number /= largest_factor
        if number > 1:
            largest_factor += 1
            if number == copy_of_num and largest_factor > upperbnd:
                return copy_of_num  
			
    return largest_factor

n = 600851475143
print "largest prime factor of ", n, "is", find_largest_prime_factor(n)

#####

########################################################################
#Problem 4 - largest palindrome that is a product of two 3-digit numbers
########################################################################


def reverse(str):
    """
    reverse a string recursively
    --input: str, the string rep of a number
    --output: reversal of str
    """
    if(len(str) <= 1):
        return str
    else:
        return str[len(str) - 1] + reverse(str[0:len(str) - 1])
    
def is_palindrome(number):
    """
    --checks if a given number is a palidrome
    --input: number, a product of two 3-digit numbers
    --output: True or False, if number is or is not palindrome
    --calls: reverse()
    """
    return (str(number) == reverse(str(number)))

def find_palindromes():
    """
    finds largest palindrome that is a product of two
    3-digit numbers. 
    Uses brute force
    """
    largest_palindrome = 0
    factor1 = 0
    factor2 = 0
    for num1 in range(100 , 1000):
        for num2 in range(num1 , 1000):
            prod = num1 * num2
            if is_palindrome(prod) and prod > largest_palindrome:
                largest_palindrome = prod
                factor1 = num1
                factor2 = num2
                
    return [largest_palindrome, factor1, factor2]
    
ret_list = find_palindromes()
print "The largest palindrome that is a prdoct of two three-digit number is", ret_list[0]
print "The factors are", ret_list[1], "and", ret_list[2]

#####



###############################################################################
#Problem 5 - smallest positive number evenly divisible by all numbers from 1-20
###############################################################################
def find_lcm(maxdivisor):
    """
    Problem 5 - Find smallest number divisible by all
    numbers from a to maxdivisor
    """
    done = False
    curr = 2
    while not done:        
        curr_divisor = 2
        while curr_divisor <= maxdivisor and curr % curr_divisor == 0:
            curr_divisor += 1
            
        if curr_divisor == maxdivisor + 1:
            done = True
        else:
            curr += 1
            
    return curr
    
n = 20
ret = find_lcm(n)
print "smallest number divisble by al numbers from 1 to", n, "is", ret


#####


######################################################################
#Problem 6 - For the first 100 positive numbers, find diff between sum 
#of squares and square of sum
######################################################################
def diff_of_sums(number):
    """
    Problem 6 - Find (sum(1:number)^2 - sum((1:number)^2)
    """
    sum_of_squares = 0
    sum_of_numbers = 0
    for count in range(1, number + 1):
        sum_of_squares += count ** 2
        sum_of_numbers += count
        
    return sum_of_numbers ** 2 - sum_of_squares

#n = 100
#ret = diff_of_sums(n)
#print "(sum(1:", n, ")^2 - sum((1:", n, ")^2) = ", ret


#####

###############################
#Problem 7 - find 10001st prime
###############################
def find_nth_prime(n):
    """
    Problem 7
    """
    primes_found = 0
    curr_num = 2
    while primes_found < n:
        if is_prime(curr_num):
            primes_found += 1
            print curr_num, primes_found
        curr_num += 1
        
    return (curr_num - 1)

def is_prime(number):
    upperbnd = int(math.ceil(math.sqrt(number)))
    for divisor in range(2, upperbnd + 1):
        if(number > 2 and number % divisor == 0):
            return False
    return True

n = 10001
ret = find_nth_prime(n)
print "prime #", n, "is", ret


########################################
#Problem 8 - Largest product in a series
#Find largest product of 13 consecutive 
#adjacent digits in a 1000 digit number
########################################

def find_max_digit_product(num_digits_in_product, numstr):
    max_prod = 0
    if num_digits_in_product <= len(numstr):
        for char in range(0, len(numstr)):
            if '0' not in numstr[char: char + num_digits_in_product]:
                res = reduce(mul, map(int, numstr[char : char + num_digits_in_product]), 1)
                if res > max_prod:
                    max_prod = res
                
    return max_prod
    
#1000 digit number
number_str = '73167176531330624919225119674426574742355349194934' + '96983520312774506326239578318016984801869478851843' + "85861560789112949495459501737958331952853208805511" + "12540698747158523863050715693290963295227443043557" + "66896648950445244523161731856403098711121722383113" +"62229893423380308135336276614282806444486645238749" + "30358907296290491560440772390713810515859307960866" + "70172427121883998797908792274921901699720888093776" +"65727333001053367881220235421809751254540594752243" +"52584907711670556013604839586446706324415722155397" +"53697817977846174064955149290862569321978468622482" +"83972241375657056057490261407972968652414535100474" +"82166370484403199890008895243450658541227588666881" +"16427171479924442928230863465674813919123162824586" +"17866458359124566529476545682848912883142607690042" +"24219022671055626321111109370544217506941658960408" +"07198403850962455444362981230987879927244284909188" +"84580156166097919133875499200524063689912560717606" +"05886116467109405077541002256983155200055935729725" +"71636269561882670428252483600823257530420752963450"
numdigits = 13
res = find_max_digit_product(numdigits, number_str)
print "max product of", numdigits, "in the given number is", res


#############################################
#Problem 9 - Find special Pythagorean triplet
#############################################
def find_pythag_triples(maxterm):
    """
    Finds all pythagogrean triples where c <= maxterm
    """
    
    max_term = maxterm
    triples_list = []
    for a in range(1, max_term + 1):
        for b in range(a, max_term + 1):
            for c in range(b, max_term + 1):
                if a ** 2 + b ** 2 == c ** 2:
                    triples_list.append((a,b,c))
    return triples_list

def check_sums_of_triples(lst, triple_sum):
    """
    Finds pythag triple with given sum in given lst
    """
    for elt in lst:
        if sum(elt) == triple_sum:
            return [elt, elt[0] * elt[1] * elt[2]]

maxterm = 1000
sum_of_terms = 1000
ret_triples = find_pythag_triples(maxterm)
ret_prod = check_sums_of_triples(ret_triples, sum_of_terms)
print "triple is", ret_prod[0], "prod is ", ret_prod[1]

#####

##########################################
#Problem 10 - Sum of all primes <= 2000000
##########################################

def is_prime(number):
    upperbnd = int(math.ceil(math.sqrt(number)))
    for divisor in range(2, upperbnd + 1):
        if(number > 2 and number % divisor == 0):
            return False
    return True
    

def sum_of_primes2(upper):
    """
    Problem 10 - Sum of all primes below upper
    """
    sum = 0
    for number in range(2, upper + 1):
        sum += is_prime(number) * number
    return sum

#maxprime = 2000000 #142913828922
maxprime = 25
ret = sum_of_primes2(maxprime)
print "sum of primes <= ", maxprime, " = ", ret

##############################################################
#Problem 10 - alternate solution, reading in text file primes
##############################################################

f = open("primes1.txt", "r") #open in read mode
data =  f.read()
f.close()

data = data.split()
data = map(int, data)
print data[1:10]

primesum = 0
maxprime = 2000000
for num in data:
    if num <= maxprime:
        primesum += num
    else:
        break

print "sum of primes <= ", maxprime, "is", primesum


#
##
###
####
#####
####
###
##
#

def find_nth_prime(number):
    """
    Problem 7 - Find the nth prime
    """
    upper = 100000
    num_list = range(2 , upper + 1)
    
    for num in num_list:
        for num2 in num_list:
            if num2 > num and num2 % num == 0:
                num_list.remove(num2)
                
    return [num_list, upper]    
    
#ret = find_nth_prime(10)
#print "there are", len(ret[0]), "primes not exceeding", ret[1]
#f = open("primes.txt", "w") #open in write mode
#for item in ret[0]:
#    f.write(str(item) + "\n")
#
#f.close()

###
"""
Project Euler
Author: David Schonberger
Created: 10/4/2014
"""
import math
from operator import mul
from numpy import *
#import timeit

def sum_multiples(upperbnd):
    """
    Problem 1: Find sum of all multiples of 3 or 5 below upperbnd
    """
    total = 0
    for count in range(1 , upperbnd):
        if(count % 3 == 0 or count % 5 == 0):
            total += count
    return total
    
#n = 1000
#print "sum of multiple of 3 or 5 under ", n, "is", sum_multiples(n)

#####

def sum_even_fibonacci(upperbnd):
    """
    Problem 2: sum of all even fibonacci <= 4000000
    """
    fib1 = 1
    fib2 = 2
    fib_sum = 2
    fib = fib1 + fib2
    while(fib <= upperbnd):
        if fib % 2 == 0:
            fib_sum += fib
        fib1 = fib2
        fib2 = fib
        fib = fib1 + fib2
    return fib_sum

#n = 4000000
#ret = sum_even_fibonacci(n)
#print "sum of even fibonacci numbers <= ", n, "is", ret

#####

def find_largest_prime_factor(number):
    copy_of_num = number
    upperbnd = int(math.ceil(math.sqrt(number)))
    largest_factor = 2
    while number > 1:
        while (number % largest_factor == 0):
            number /= largest_factor
        if number > 1:
            largest_factor += 1
            if number == copy_of_num and largest_factor > upperbnd:
                return copy_of_num  
			
    return largest_factor

#n = 600851475143
#print "largest prime factor of ", n, "is", find_largest_prime_factor(n)

#####
#import math
def prime_list(n):
    factor = 2
    primelist = {}
    while (n > 1):
        while(n % factor == 0):
            n /= factor
            if str(factor) in primelist.keys():
                primelist[str(factor)] += 1
            else:
                primelist[str(factor)]  = 1
        factor += 1
    return primelist
    
#n = 10000
#print prime_list(n)


#####

def find_lcm(maxdivisor):
    """
    Problem 5 - Find smallest number divisible by all
    numbers from a to maxdivisor
    """
    done = False
    curr = 2
    while not done:        
        curr_divisor = 2
        while curr_divisor <= maxdivisor and curr % curr_divisor == 0:
            curr_divisor += 1
            
        if curr_divisor == maxdivisor + 1:
            done = True
        else:
            curr += 1
            
    return curr
    
#n = 20
#ret = find_lcm(n)
#print "smallest number divisble by al numbers from 1 to", n, "is", ret

#####
    
def diff_of_sums(number):
    """
    Problem 6 - Find (sum(1:number)^2 - sum((1:number)^2)
    """
    sum_of_squares = 0
    sum_of_numbers = 0
    for count in range(1, number + 1):
        sum_of_squares += count ** 2
        sum_of_numbers += count
        
    return sum_of_numbers ** 2 - sum_of_squares

#n = 100
#ret = diff_of_sums(n)
#print "(sum(1:", n, ")^2 - sum((1:", n, ")^2) = ", ret

#####
        
    
def find_nth_prime(number):
    """
    Problem 7 - Find the nth prime
    """
    upper = int(math.ceil(math.sqrt(number)))
    num_list = range(2 , upper + 1)
    
    for num in range(2, upper + 2):
        for num2 in num_list:
            if num2 > num and num2 % num == 0:
                num_list.remove(num2)
                
    return [num_list, upper]    
    
#ret = find_nth_prime(100)
#print "there are", len(ret[0]), "primes not exceeding", ret[1]
#f = open("primes.txt", "w") #open in write mode
#for item in ret[0]:
#    f.write(str(item) + "\n")
#
#f.close()

#####

#s = """\
#import timeit
#import math
#def prime_sieve(n):
#    
#    #Return list of primes <= n
#    
#    upper = int(math.ceil(math.sqrt(n)))
#    lst = range(2, n + 1)
#    for num in range(2 , upper + 2):
#        for num2 in lst:
#            if num2 > num and num2 % num == 0:
#                lst.remove(num2)
#    return lst
#    
#ret = prime_sieve(40000)
#print len(ret)
#"""
#timeit.timeit(stmt = s, number = 1)


#####

def find_nth_prime2(n):
    """
    Problem 7
    """
    primes_found = 0
    curr_num = 2
    while primes_found < n:
        if is_prime(curr_num):
            primes_found += 1
            print curr_num, primes_found
        curr_num += 1
        
    return (curr_num - 1)

def is_prime(number):
    upperbnd = int(math.ceil(math.sqrt(number)))
    for divisor in range(2, upperbnd + 1):
        if(number > 2 and number % divisor == 0):
            return False
    return True

#n = 10001
#ret = find_nth_prime2(n)
#print "prime #", n, "is", ret

#####

def find_max_digit_product(num_digits_in_product, numstr):
    max_prod = 0
    if num_digits_in_product <= len(numstr):
        for char in range(0, len(numstr)):
            if '0' not in numstr[char: char + num_digits_in_product]:
                res = reduce(mul, map(int, numstr[char : char + num_digits_in_product]), 1)
                if res > max_prod:
                    max_prod = res
                
    return max_prod

#number_str = '73167176531330624919225119674426574742355349194934' + '96983520312774506326239578318016984801869478851843' + "85861560789112949495459501737958331952853208805511" + "12540698747158523863050715693290963295227443043557" + "66896648950445244523161731856403098711121722383113" +"62229893423380308135336276614282806444486645238749" + "30358907296290491560440772390713810515859307960866" + "70172427121883998797908792274921901699720888093776" +"65727333001053367881220235421809751254540594752243" +"52584907711670556013604839586446706324415722155397" +"53697817977846174064955149290862569321978468622482" +"83972241375657056057490261407972968652414535100474" +"82166370484403199890008895243450658541227588666881" +"16427171479924442928230863465674813919123162824586" +"17866458359124566529476545682848912883142607690042" +"24219022671055626321111109370544217506941658960408" +"07198403850962455444362981230987879927244284909188" +"84580156166097919133875499200524063689912560717606" +"05886116467109405077541002256983155200055935729725" +"71636269561882670428252483600823257530420752963450"
#numdigits = 13
#res = find_max_digit_product(numdigits, number_str)
#print res

#####

def find_pythag_triples(maxterm):
    """
    Finds all pythagogrean triples where c <= maxterm
    """
    
    max_term = maxterm
    triples_list = []
    for a in range(1, max_term + 1):
        for b in range(a, max_term + 1):
            for c in range(b, max_term + 1):
                if a ** 2 + b ** 2 == c ** 2:
                    triples_list.append((a,b,c))
    return triples_list

def check_sums_of_triples(lst, triple_sum):
    """
    Finds pythag triple with given sum in given lst
    """
    for elt in lst:
        if sum(elt) == triple_sum:
            return [elt, elt[0] * elt[1] * elt[2]]

#maxterm = 1000
#sum_of_terms = 1000
#ret_triples = find_pythag_triples(maxterm)
#ret_prod = check_sums_of_triples(ret_triples, sum_of_terms)
#print "triple is", ret_prod[0], "prod is ", ret_prod[1]

#####

def sum_of_primes(upper):
    """
    Problem 10 - Sum of al primes below upper
    """
    prime_list = find_nth_prime(upper)[0]
    return sum(prime_list)

#takes too long to go to 2000000...try online via WAS maybe?
#maxprime = 200
#ret = sum_of_primes(maxprime)
#print "sum of primes <= ", maxprime, " = ", ret

#####


"""
Problem 10 - alternate solutions, reading in text file primes
"""
#f = open("primes1.txt", "r") #open in read mode
#data =  f.read()
#f.close()
#data = data.split()
#data = map(int, data)
#print data[1:10]
#
#primesum = 0
#maxprime = 2000000
#for num in data:
#    if num <= maxprime:
#        primesum += num
#    else:
#        break
#
#print "sum of primes <= ", maxprime, "is", primesum


#####    

def sum_of_primes2(upper):
    """
    Problem 10 - Sum of all primes below upper
    """
    sum = 0
    for number in range(2, upper + 1):
        sum += is_prime(number) * number
    return sum

#maxprime = 2000000 #142913828922
#maxprime = 25
#ret = sum_of_primes2(maxprime)
#print "sum of primes <= ", maxprime, " = ", ret

#####

"""
Problem 11 - largest product in a grid
Input: a 20 by 20 grid of numbers in [0, 99]
Output: greatest product of 4 adjacent numbers 
in a row, col or on a diag
"""

def max_4_prod_row(arr):
    """
    Find largest product of 4 in any row
    """
    nrows = arr.shape[0]
    ncols = arr.shape[1]
    max_prod = 0
    max_terms = []
    for row_idx in range(0, nrows):
        for col_idx in range(0, ncols - 3):
            
            currprod = reduce(mul, arr[row_idx, col_idx : col_idx + 4])
            if currprod > max_prod:
                max_prod = currprod
                max_terms = [arr[row_idx, col_idx : col_idx + 4]]
            
    return [max_prod, max_terms]
    
def max_4_diag_prod(arr):
    """
    returns max prod of 4 adjacent along any *descending* diag
    """
    nrows = arr.shape[0]
    ncols = arr.shape[1]
    max_prod = 0
    max_terms = []
    for row_idx in range(0, nrows - 3):
        for col_idx in range(0, ncols - 3):
            
            curr_prod = arr[row_idx, col_idx] * \
            arr[row_idx + 1, col_idx + 1] * \
            arr[row_idx + 2, col_idx + 2] * \
            arr[row_idx + 3, col_idx + 3]
            if curr_prod > max_prod:
                max_prod = curr_prod
                max_terms = [arr[row_idx, col_idx], \
                arr[row_idx + 1, col_idx + 1], \
                arr[row_idx + 2, col_idx + 2], \
                arr[row_idx + 3, col_idx + 3]]
            
    
    return [max_prod, max_terms]

def max_4_diag_prod2(arr):    
    """
    returns max prod of 4 adjacent along any *ascending* diag
    """
    nrows = arr.shape[0]
    ncols = arr.shape[1]
    max_prod = 0
    max_terms = []
    for row_idx in range(3, nrows):
        for col_idx in range(0, ncols - 3):
            curr_prod = arr[row_idx, col_idx] * \
            arr[row_idx - 1, col_idx + 1] * \
            arr[row_idx - 2, col_idx + 2] * \
            arr[row_idx - 3, col_idx + 3]
            if curr_prod > max_prod:
                max_prod = curr_prod
                max_terms = [arr[row_idx, col_idx], \
                arr[row_idx - 1, col_idx + 1], \
                arr[row_idx - 2, col_idx + 2], \
                arr[row_idx - 3, col_idx + 3]]
    
    return [max_prod, max_terms]

#grid_str = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08" + " 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00" +" 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65" + " 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91" +" 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80" +" 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50" +" 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70" +" 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21" +" 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72" +" 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95" +" 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92" +" 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57" +" 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58" +" 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40" +" 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66" +" 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69" +" 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36" +" 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16" +" 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54" +" 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
#grid_str = grid_str.split()
#grid_num = map(int, grid_str)
#num_arr = array(grid_num)
#num_arr = num_arr.reshape(20,20)
#rowmax = max_4_prod_row(num_arr)
#colmax = max_4_prod_row(num_arr.transpose())
#diagmax = max_4_diag_prod(num_arr)
#diagmax2 = max_4_diag_prod2(num_arr)
#print num_arr
#print rowmax[0]
#print colmax[0]
#print diagmax[0]
#print diagmax2[0]
#48477312
#51267216
#40304286
#70600674

"""
Problem 12 - highly divisble triangular number
Find value of first triangular # with > 500 divisors
"""
def triangular_num_divisor_count(threshold):
    """
    Find smallest triangular number with more 
    divisors than threshold
    """
    divisor_count = 1
    curr_tri_num = 0
    tri_num_idx = 2
    while divisor_count < threshold:
        curr_tri_num = tri_num_idx * (tri_num_idx + 1) / 2
        prime_fac_list = prime_list(curr_tri_num)
        for v in prime_fac_list.values():
            divisor_count *= (v + 1)
        if divisor_count < threshold:
            divisor_count = 1
        tri_num_idx += 1
        
    return curr_tri_num
    
#ret = triangular_num_divisor_count(500)
#print ret

#tn = 842161320
#prime_fac_list = prime_list(tn)
#print prime_fac_list

"""
Problem 13 - find first ten digits of sum of 
100 50-digit #s
"""
def number_sum():
    lst = []
    f = open("fifty_digit_numbers.txt", "r") #open in write mode

    lst.append(f.read())
    f.close()
    numlst = lst[0].split('\n')
    numlst = map(int, numlst)
    cumulsum = 0
    for elt in numlst:
        cumulsum += elt
    return cumulsum
    
#print number_sum()
#5537376230390876637302048746832985971773659831892672

#####
"""
Problem 14 - longest collatz seq
which starting number under 1,000,000 
produces the longest collatz seq
"""

def get_collatz_seq_len(start):
    num = start
    seq_len = 1
    #print "start:", start
    #print num
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        seq_len += 1
     #   print num
    #print "len:", seq_len
    #print "###"
    
    return seq_len

def find_longest_collatz(upper):
    max_seq_len = 0
    startnum = 0
    for num in range(2, upper + 1):
        seqlen = get_collatz_seq_len(num)
        if seqlen > max_seq_len:
            max_seq_len = seqlen
            startnum = num
    return [max_seq_len, startnum]
                
n = 1000000
ret = find_longest_collatz(n)
print ""
print ret[0], ret[1]

###
"""
problem 16 - sum of digits of 2^1000
"""
n = 2 ** 1000
nstr = str(n)
digsum = 0
for d in nstr:
    digsum += int(d)
print digsum
