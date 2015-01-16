"""
David Schonberger
Project Euler - problem 59
XOR decryption
"""
fp = "C:/Users/David/Documents/TechStuff/OnlineCourses/ProjectEuler/"
fn_out =  "decipher.txt"
fn_in = "cipher.txt"

cipher_text = []
with open(fp+fn_in) as f:
    for line in f:
        cipher_text.append(line.split(","))

l = len(cipher_text[0]) / 3
r = len(cipher_text[0]) % 3
remove_chrlst = ["]","[","~","`","{","}","%","&", "@", "#", "-","/", "$", "^", "*", "=", "+", ">", "<"]

decryptions = []
for i in range(97,123):
    for j in range(97,123):
        for k in range(97,123):
            key = l * [i,j,k]
            if(r == 1):
                key.append(i)
            elif(r == 2):
                key += [i,j]
            plain_text = map(lambda pair: chr(int(pair[0])^pair[1]), zip(cipher_text[0], key))
            if sum([ch in plain_text for ch in remove_chrlst]) == 0:
                decryptions.append(plain_text)

print sum([ord(ch) for ch in decryptions[0]])

###
#f = open(fp+fn_out,'w')
#for i in range(len(decryptions)):
#    decryption_str = ""
#    for j in range(len(decryptions[i])):
#        decryption_str += decryptions[i][j]
#        
#    f.write(decryption_str + "\n")
#f.close()            
