"""
David Schonberger
Project Euler - problem #19, 20
19) Count # of sundays that fell on
1st of month from 1/1/1900 through 12/31/2000

20) Find sum of digits of 100!

Solved : 11/30/2014
"""
from datetime import date 
from datetime import timedelta
import math
begin_date = date(1901 , 1 , 1)
end_date = date(2000, 12 , 31)
td = timedelta(days = 1)

sunday_count = 0
while begin_date <= end_date:
    if begin_date.weekday() == 6 and begin_date.day == 1:
        sunday_count += 1
    begin_date += td
    
print sunday_count


x = str(math.factorial(100))
print x
print len(x)
digit_sum = 0
for ch in x:
    digit_sum += int(ch)

print digit_sum