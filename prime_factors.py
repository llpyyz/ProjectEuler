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