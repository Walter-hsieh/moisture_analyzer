# with open("a_1_sec.txt", 'r') as f:
# 	for line in f:
# 		print(line)


with open("mof-801_1_sec.txt", 'r') as f:
	last_line = f.readlines()[-4].split()[1]
	print(last_line, type(last_line))