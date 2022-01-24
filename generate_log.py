#Given : 10Racks, 10Data Nodes per rack, 100000 Files, 10k blocks per file in DFS.
#Task : Generate DFS using Hadoop replication factors

#Importing necessary libraries
from distutils.command.build_scripts import first_line_re
import random
import sys
import functools
import os

#Opening an empty text file and accessing write permission
log={}

no_of_racks = 10
no_of_datanodes = 10
no_of_files = 1000
no_of_blocks = 100

f= open("disk_log.txt","w")

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

# print(f"Type of each element in file_blocks is {type(file_blocks[0])}")
# print(type(list(file_blocks[0].values())))


for i in file_blocks:
	print(type(i))
	for j in list(i.values()):
		print(type(j))
		for k in j:
			print(type(k))
			racks = random.sample(data_node,2)
			print(racks)
			first_rack = racks[0]
			
			nodes = random.sample(list(first_rack.values())[-1],2)
			first_node = nodes[0]
			second_node = nodes[1]
			# print(first_rack[-1].keys())
			# list(first_rack[-1].values())[-1].remove(first_node[-1])
			# second_node = nodes[1]
			# z = data_node
			# z.remove(first_rack[-1])
			# third_rack = random.sample(z,1)
			second_rack = racks[1]
			third_node = random.sample(list(second_rack.values())[-1],1)
			s = f"{j}  {k} {first_node} {second_node} {third_node}\n"
			f.write(s)

f.close()



