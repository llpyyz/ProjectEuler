"""
David Schonberger
Project Euler - problem #18, 67
'Maximum sum path, I and II'
Find max total from top to bottom
of a given pyramid of numbers with
i numbers in row i.

Solved : 11/28/2014
"""

import random
import math
import copy

#return list with T_n (nth triangular number)
#random elements between low and high inclusive
def make_random_list(n, low, high):
    ret_lst = []
    for idx in range(n * (n+1) / 2):
        ret_lst.append(random.randint(low, high))
    return ret_lst

def make_triang_sublists(lst, nr):
    sublists = []
    for i in range(nr):
        tmp_lst = []
        for j in range( i * (i + 1) / 2, i * (i + 1) / 2 + i + 1):
            tmp_lst.append(lst[j])
        sublists.append(tmp_lst)
    return sublists
    
#represent an n row triangle as a list whose size is
#the nth triamgular number, e.g. 15 rows -> t_15 = 120 elts
prob_18_lst = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65,19, 01, 23 ,75 ,3, 34,
88, 2, 77, 73, 7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92,41, 41, 26, 56, 83, 40, 80, 70, 33,
41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,
70, 11, 33, 28, 77, 73, 17, 78, 39, 68 ,17, 57,91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,
63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

nr = int((-1 + math.sqrt(1 + 8 * len(prob_18_lst)))/2)
#triang_sublists = make_triang_sublists(prob_18_lst, nr)

fp = "C:/Users/David/Documents/TechStuff/OnlineCourses/ProjectEuler/"
fn = "triangle.txt"
prob_67_lst = []
with open(fp+fn) as f:
    for line in f:
        prob_67_lst.append(line.split())

for i in range(len(prob_67_lst)):
    for j in range(len(prob_67_lst[i])):
        prob_67_lst[i][j] = int(prob_67_lst[i][j])

low = 1
high = 100
nr = 100
rnd_lst = make_random_list(nr, low , high)
#triang_sublists = make_triang_sublists(rnd_lst, nr)
triang_sublists = copy.deepcopy(prob_67_lst)

lst_copy = []
for i in range(len(triang_sublists) - 1):
    if i == 0:
        lst_copy.append(list(triang_sublists[i]))
        extend_right = 2 * lst_copy[i]
        tmp = [x + y for x,y in zip(extend_right, triang_sublists[i+1])]
        lst_copy.append(tmp)
        
    elif len(triang_sublists) > 2:
        
        #broadcast curr row to next by extending it on right and left
        #then adding to next row and taking max of these two
        l = len(lst_copy[i])
        extend_right = lst_copy[i] + [lst_copy[i][l-1]]
        extend_left = [lst_copy[i][0]] + lst_copy[i]
        tmp1 = [x + y for x,y in zip(extend_right, triang_sublists[i+1] )]
        tmp2 = [x + y for x,y in zip(extend_left, triang_sublists[i+1] )]
        max_lst = [max(elt) for elt in zip(tmp1, tmp2)]
        lst_copy.append(max_lst)
        
print "\nFinal lst, with max path sums ", lst_copy[nr-1] , "\n"
print "Max path sum = ", max(lst_copy[len(lst_copy) - 1]), "\n"




#l1 = [6,2,8]
#l2 = [3,5,9]
#z = zip(l1,l2)
#print z
#print [max(elt) for elt in z], l1, l2
#
#
#l1 = [6,2,8]
#l2 = [3,5,9]
#l3 = [1,2,3]
#l4 = [5,6,7]
#print zip(l1,l2, l3, l4)
#
#biglst = [l1, l2, l3, l4]

#l = [1,2,3]
#m =  [5,6,7]
#print [x + y for x, y in zip(l,m)]

