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
		
		
		z = data_node
		z.remove(random_rack[-1])
		third_rack = random.sample(z,1)
		third_node = random.sample(list(third_rack[-1].values())[-1],1)
		print(third_node)
		# print(list(random_rack[-1].values())[-1])


print(f"\n\n\n{data_node}")

