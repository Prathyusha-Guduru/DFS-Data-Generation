import random

f = open('min_output.txt',"r")

r = ['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10']
d = ['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10']



random_rd = random.choices(r,k=1)[-1]+random.choices(d,k=1)[-1]
print(type(random_rd))