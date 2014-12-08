import math

def is_prime(n):
    if n < 0:
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
    
def eval_quad(n, a, b):
    return n ** 2 + a * n + b

max_primes = 0
a = 1000
b = 1000
coeff_info = []
final_primes_lst = []
for i in range(1 , a):
    
    for j in range(2 , b):
        if is_prime(j):
            n = 0
            curr_primes_count = 0
            curr_primes_lst = []
            while(is_prime(eval_quad(n,-i,j))):
                curr_primes_lst.append(eval_quad(n,-i,j))
                n += 1
                curr_primes_count += 1
                
            if(curr_primes_count > max_primes):
                coeff_info = [-i,j,-i*j]
                max_primes = curr_primes_count
                final_primes_lst = list(curr_primes_lst)
            
print "***\nlargest list of primes:",final_primes_lst, "\n", len(final_primes_lst)
print "final max coeff prod:", coeff_info

#for a, b >0, coeff prod = 41, a = 1, b = 41
#for a <0, b >0, coeff prod = -59231, a = -61, b = 971