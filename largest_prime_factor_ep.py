#########################################
#Project Euler https://projecteuler.net/
#########################################

#################################################
#Problem 3 - largest prime factor of 600851475143
#################################################
import math
import codeskulptor

number = 600851475143

def find_largest_prime_factor(number):
    copy_of_num = number
    upperbnd = int(math.ceil(math.sqrt(number)))
    largest_factor = 2
	while number > 1:
	    while (number % largest_factor == 0):
		    number /= largest_factor
		if number > 1:
		    largest_factor += 1
			if number == copy_of_num and largest_factor > upperbnd: #number is prime
			    return copy_of_num  
			
    return largest_factor

print "largest prime factor of ", number, "is", find_largest_prime_factor(number)

