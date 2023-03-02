#The python application above is able to log and retrieve values from the DAQ sensor
#It is also plotting the values and saving them into the .txt file
#However this program does not upload data in real time, my more advanced program(2) does this which is something I had to implement later on

import numpy as np
import matplotlib.pyplot as plt #This is imported because we will plot the values we are taking
import time 
import nidaqmx

#This initializes the logging 
time_to_stop = 30 #Programming running for 30 seconds, for example
sampling_time = 1 #sampling time is set at 1 second
n = int(time_to_stop/sampling_time)
data = [] #data is stored as an array so we can plot in the future

#This initializes connected DAQ device 
task = nidaqmx.Task()
task.ai_channels.add_ai_thrmcpl_chan("ex") #Thermocouple channel can be set to whichever channel
task.start()

#Open File which will be used to input recorded data 
file = open("temp_of_data.txt", "w")

#Writes data function class
def writeFileData(t,x):
    time = str(t)
    value = str(round(x,2))
    file.write(time + "\t" + value)
    file.write("\n")

#This logs the temperature data from the DAQ device
for i in range(n):
    value = task.read() #logging data from temperature sensor 
    print("Temperature =", round(value,1), "[]")
    data.append(value) #adding to our array 
    time.sleep(time_to_stop)
    writeFileData(i*sampling_time, value) #writing temperature values to the text file

#This stops the DAQ after it is done collecting
task.stop()
task.close()

#Closing the file
file.close()

#This is the script for plotting our values 
t = np.arange(0,time_to_stop, sampling_time)
plt.plot(t,data,"-o")
plt.title('Temperature Values')
plt.xlabel('t[s]')
plt.ylabel('Temperature in degC')
plt.grid()
Tmin = 0
Tmax = 30
plt.axis([0,time_to_stop,Tmin,Tmax])
plt.show()