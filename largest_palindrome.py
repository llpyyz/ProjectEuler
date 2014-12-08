#########################################
#Project Euler https://projecteuler.net/
#########################################

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

