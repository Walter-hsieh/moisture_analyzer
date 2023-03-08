import time
import serial
import matplotlib.pyplot as plt
import datetime

# 與設備通訊
ser = serial.Serial(
    port='COM3',
    baudrate=1200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
    )

# 確認是否連上設備
if (ser.isOpen() == 0):
    ser.open()

state = ser.isOpen()
print('state: ' + str(state))
print('connection succeeded.') 

sample_name = input("Enter the sample name: ")
t = int(input("Enter time in second: "))

# 倒數時間/模組
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


filename = sample_name + '_' +str(t) + '_sec.txt'

with open(filename,'w') as f:
    pass

ser.write('START\r'.encode('utf-8'))



data = [0]

weight = []


count = 0

while True:
    recorder = open(filename,'a')
    out = ser.read().decode('utf-8')
    recorder.write(out)
    f.close()
    count += 1

    print(count)



    if count > 500:

        with open(filename, 'r') as f:
            last_line = f.readlines()[-2].split()

            if data[-1] != last_line:

                data.append(last_line)
                f.close()
                print(data[-1][1])
                weight.append(float(data[-1][1]))




            plt.plot(weight, marker='.')
            plt.draw()
            plt.pause(0.0001)
            plt.savefig(filename.replace('txt', 'png'))
            plt.clf()



# https://www.codingem.com/how-to-read-the-last-line-of-a-file-in-python/


