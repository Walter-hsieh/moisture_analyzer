import pandas as pd
import matplotlib.pyplot as plt



# oepn txt file and read lines

def read_txt():
	with open("test_dataset.txt", 'r') as f:
		last_line = f.readlines()[-4].split()[1]
		print(last_line, type(last_line))


data = {'time':[], 'gram':[]}


# make into dataframe with pandas
with open("test_dataset.txt", 'r') as file:
	lines = file.readlines()

	for line in lines[16:len(lines)-4]:
		time, gram = line.split()
		data['time'].append(time)
		data['gram'].append(float(gram))

df = pd.DataFrame(data)

print(df.head())

plt.plot(df['gram'])
plt.show()

