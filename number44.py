"""
David Schonberger
Project Euler - problem 44
Pentagon numbers
"""

def check_pent_num(n):
    is_pent_num = False
    curr_pent_num = 0
    i = 1
    while(not is_pent_num and curr_pent_num <= n):
        curr_pent_num = i*(3*i-1)/2
        if(n == curr_pent_num):
            is_pent_num = True
        i += 1
    
    return is_pent_num

pent_num_count = 2501
pent_num_lst = []
for i in range(1,pent_num_count):
    pent_num_lst.append(i*(3*i-1)/2)
    
min_diff = pent_num_lst[pent_num_count - 2]
diff_count = 0
sum_list = []
for i in range(len(pent_num_lst)):
    for j in range(i + 1,len(pent_num_lst)):
        pn_diff = abs(pent_num_lst[i] - pent_num_lst[j])
        pn_sum = pent_num_lst[i] + pent_num_lst[j]
        if(pn_diff in pent_num_lst):
            diff_count += 1
            sum_list.append([pent_num_lst[i], pent_num_lst[j]])
            if(check_pent_num(pn_sum)):
                if(pn_diff < min_diff):
                    min_diff = pn_diff
                    
print min_diff, pent_num_lst[pent_num_count - 2]
print "for the first", pent_num_count-1, "pent nums", diff_count, "diff in pent list\n"
cnt = 0
for elt in sum_list:
    if(check_pent_num(elt[0] + elt[1])):
        cnt += 1
        print elt, check_pent_num(elt[0] + elt[1])
    
print "\ncount:\n",cnt

#[1560090, 7042750] 5482660 = min diff
