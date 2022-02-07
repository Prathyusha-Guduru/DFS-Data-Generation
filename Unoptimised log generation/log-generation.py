
import random
import re
import string
from collections import defaultdict

output = open('output.txt')
re_rd = r'''R[0-9]{1,4}D[0-9]{1,4}'''
count = 0
output = output.read().splitlines()



log_string = []
f= open("min_output.txt","w")
rd_lines = []
for i,lines in enumerate(output):
	
		if(re.search(re_rd,lines) != None) :
			# f.write(f"{re.match(re_rd, lines).group(0)} {output[i+(random.randint(0,10))]} {output[i+(random.randint(20,40))]} {output[i+(random.randint(50,80))]} {output[i+(random.randint(80,100))]} {output[i+(random.randint(40,50))]}\n")
			# log_string.append(f"{re.match(re_rd, lines).group(0)} {output[i+(random.randint(0,10))]} {output[i+(random.randint(20,40))]} {output[i+(random.randint(50,80))]} {output[i+(random.randint(80,100))]} {output[i+(random.randint(40,50))]}\n")
			rd_lines.append(i)

f.close()

# print(output[rd_lines[4]].split("\t")[0])

for i in rd_lines:
	print(i)

# print(type((log_string[0]).split("\t")))

# dict_list = []
# for i in log_string:
# 	d = {i.split("\t")[0] : i.split("\t")[1:]}
# 	dict_list.append(d)
# print(dict_list[0])

# r = ['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10']
# d = ['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10']


# res = defaultdict(list)
# for sub in dict_list:
#     for key in sub:
#         res[key].append(sub[key])
	
# log_txt = open("log.txt","w")
# for i in range(0,10000):
	
# 	random_rd = random.choices(r,k=1)[-1]+random.choices(d,k=1)[-1]+" "
# 	if(random_rd in res):
# 		log_txt.write(f"{random_rd} {res[random_rd]}\n")

# log_txt.close()
