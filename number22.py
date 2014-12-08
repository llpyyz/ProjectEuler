"""
David Schonberger
Project Euler - problem #22
Names scores

Read in a list of first names in a text file
Sort the names in asc alphabetical order.
The score for a name is its position in the sorted
list times its value. The value is determined using
the standard a -> 1, b -> 2, ..., z -> 26 mapping and
is equal to the sum of the values for each letter in the 
name.

Calculate the total of all name scores in the list

Solved : 11/30/2014
"""

def str_to_value(s):
    val = 0
    for ch in s:
        val += ord(ch) - 96
    return val

fp = "C:/Users/David/Documents/TechStuff/OnlineCourses/ProjectEuler/"
fn =  "names.txt"
total_score = 0
name_lst = []
with open(fp+fn) as f:
    for line in f:
        name_lst.append(line.split(","))

for i in range(len(name_lst[0])):
    name_lst[0][i] = name_lst[0][i].replace('"', '').lower()
    
name_lst[0].sort()

idx = 1
for elt in name_lst[0]:
    total_score += str_to_value(elt) * idx
    idx += 1

print total_score
