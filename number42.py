"""
David Schonberger
Project Euler - problem #42
Coded triangle numbers
"""
fp = "C:/Users/David/Documents/TechStuff/OnlineCourses/ProjectEuler/"
fn =  "words.txt"
word_lst = []
split_list = []
triangle_word_count = 0

def str_to_value(s):
    val = 0
    for ch in s:
        val += ord(ch) - 96
    return val

def is_square(n):
    square = False
    i = 1
    while(i ** 2 <= n and not square):
        if(i ** 2 == n):
            square = True
        i += 1
    
    return square
    
with open(fp+fn) as f:
    for line in f:
        word_lst.append(line.split(","))

for i in range(len(word_lst[0])):
    split_list.append( word_lst[0][i].replace('"', '').lower())

for elt in split_list:
    word_score = 0
    for c in elt:
        word_score += str_to_value(c)
    if(is_square(1 + 8 * word_score)):
        triangle_word_count += 1

print triangle_word_count