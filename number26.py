import decimal
decimal.getcontext().prec = 200
fp = "C:/Users/David/Documents/TechStuff/OnlineCourses/ProjectEuler/"
fn = "decimal.txt"
d = 1000
f = open(fp+fn, 'w+')
for i in range(1,d):
    f.write(str(d) + ": " + str(decimal.Decimal(1) / decimal.Decimal(i)) + "\n")
    
f.close()