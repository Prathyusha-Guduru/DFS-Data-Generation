#Given : 10Racks, 10Data Nodes per rack, 100000 Files, 10k blocks per file in DFS.
#Task : Generate DFS using Hadoop replication factors

#Importing necessary libraries
from distutils.command.build_scripts import first_line_re
import random
import sys
import functools
import os

#Opening an empty text file and accessing write permission
f= open("disk.txt","w")
log={}

no_of_racks = 10
no_of_datanodes = 10
no_of_files = 5
no_of_blocks = 2


racks = []
for i in range(0,no_of_racks):
	racks.append(f"R{i}")

data_node = []
for i in range(0, len(racks)):
	rack = {}
	rack[f"R{i}"] = []
	for j in range(0,no_of_datanodes):
		rack[f"R{i}"].append(f"R{i} D{j}")
	data_node.append(rack)



files = []
for i in range(0,no_of_files):
	files.append(f"F{i}")


file_blocks = []
for i in range(0,len(files)):
	blocks = {}
	blocks[f"F{i}"] = []
	for j in range(0,no_of_blocks):
		blocks[f"F{i}"].append(f"F{i}B{j}")
	file_blocks.append(blocks)



for i in file_blocks:
	for j in i.values():
		random_rack = random.sample(data_node,1)
		random_node = random.sample(list(random_rack[-1].values())[-1],1)
		print(random_node)

		second_node = random.sample(list(random_rack[-1].values())[-1],1)
		if(second_node != random_node):
			print(f"second node {second_node}")
		else:
			second_node = random.sample(list(random_rack[-1].values())[-1],1)
			print(f"second node {second_node}")
		
		if(random_rack[-1] in data_node):
			print("YES")
		else:
			print("SORRY!")
		print(f"first rack is {random_rack}")
		# third_rack = random.sample(data_node.remove(random_rack),1)
		# third_node = random.sample(list(third_rack[-1].values())[-1],1)
		# print(third_node)
		# print(list(random_rack[-1].values())[-1])


print(f"\n\n\n{data_node}")






# for i in range(1,10):
# 	log["F"+str(i)]=[]
# 	for j in range(1,5):         #10 blocks
# 		k=random.randint(0,9)      #1000 Files,100 Blocks per each File
# 		l=random.randint(0,9)       #10 Racks,10 Datanodes
# 		m=random.randint(1,10)     #Each Block Replication Factor=3
# 		n=random.randint(1,10)
# 		o=random.randint(1,10)
# 		while k==m:
# 			m=random.randint(1,10)
# 		s="F"+str(i)+" "+"F"+str(i)+"B"+str(j)+" "+"R"+str(k)+"D"+str(l)+" "+"R"+str(k)+"D"+str(o)+" "+"R"+str(m) +"D"+str(n)

# 		log["F"+str(i)].append(["B"+str(j),"R"+str(k),"D"+str(l),"R"+str(k),"D"+str(o),"R"+str(m),"D"+str(n)])

# 		f.write(s+'\n')
# print("Disk is ready")
# #print(Disk)

# f.close()
