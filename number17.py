"""
David Schonberger
Project Euler - problem #17
'Number letter counts'
If all the numbers from 1 to 1000 incl
are written out in words, how many letters?
Ignore spaces and hyphens; use 'and'
for numbers > 100, e.g 274 is 'two hundred AND seventy four'
as per accepted U.K. spelling

Solved : 11/28/2014
"""
units = {1:'one', 2:'two', 3: 'three', 4 : 'four', 5 : 'five', 6: 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
teens = {10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen'}
higher_tens = {20 : 'twenty', 30 :'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}
hundred =  'hundred'
thousand =  'thousand'
and_str = 'and'

def get_units(n):
    return n % 10

def get_digit(n, power):
    if n < 10 ** (power + 1):
        return n / (10 ** power)
    else:
        return (n % (10 ** (power + 1)) ) / (10 ** power)

def get_under_100(i, ones, tens):
    if i < 10:
        return units[ones]
    elif i < 20:
        return teens[tens * 10 + ones]
    else:
        if i % 10 == 0:
            return higher_tens[tens * 10]
        else:
            return higher_tens[tens * 10] + units[ones]

### driver code ###

low = 1
high = 1000
count = 0
for i in range(low, high + 1):
    ones = get_units(i)
    tens = get_digit(i,1)
    hundreds = get_digit(i,2)
    thousands = get_digit(i,3)
    
    if i < 100:
        word = get_under_100(i, ones, tens)
        count += len(word)
    elif i < 1000:
        if i % 100 == 0:
            word = units[hundreds] + hundred
            count += len(word) 
        else:
            word = units[hundreds] + hundred + and_str + get_under_100(i % 100, ones, tens)
            count += len(word)
    else:
        word = units[thousands] + thousand
        count += len(word)
    
    print word

print count, "\n"
