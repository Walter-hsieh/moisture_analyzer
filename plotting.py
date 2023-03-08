import matplotlib.pyplot as plt
import time

# 倒數時間/模組
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1



def make_plot():
	filename = input("filename:  ")


	data = [0]

	weight = []

	while True:
		with open(filename, 'r') as f:
		    last_line = f.readlines()[-2].split()

		    if data[-1] != last_line:

		        data.append(last_line)
		        f.close()
		        try:
		        	weight.append(float(data[-1][1]))
		        except:
		        	continue




		    plt.plot(weight, marker='.')
		    plt.draw()
		    plt.pause(0.0001)
		    plt.savefig(filename.replace('txt', 'png'))
		    plt.clf()

		countdown(1)

make_plot()