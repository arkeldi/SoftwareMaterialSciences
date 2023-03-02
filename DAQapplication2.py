#This updated script has that for each logging reading reading from the temperature device, the plot is updated in real time

import matplotlib.pyplot as plt #This is imported because we will plot the values we are taking
import time 
import nidaqmx
import matplotlib.animation as animation #Had to use this module to make the program upload in real time

def read_daq(): #Python function for reading from the DAQ, writing function stems from reading 
    task = nidaqmx.Task()
    task.ai_channels.add_ai_thrmcpl_chan("TC01/ai0")
    task.start()
    value = task.read()
    task.stop()
    task.close()
    return value

#Writes data function class
def writeFileData(t,x):
    file = open("temp_of_data.txt", "w") #Open File which will be used to input recorded data 
    time = str(t) #We begin to write the data 
    value = str(round(x,2))
    file.write(time + "\t" + value)
    file.write("\n")
    file.close() #Closing the file

#Initialize logging
sampling_time = 1 #sampling time is set at 1 second
numPoints = 50 #Number of points that will be displayed
k=1
length_x = numPoints
Tmin = 0
Tmax = 30
range_y = [Tmin, Tmax]
data = []

#Creating a figure to plot
figure = plt.figure()
axis = fig.add_subplot(1,1,1)
xaxis = list(range(0,numPoints))
yaxis = [0] * length_x
axis.set_ylim(range_y)

#Creating a blank line that will morph after taking in data 
line, = ax.plot(xaxis, yaxis)

#Plot script 
plt.title('Temperature Values')
plt.xlabel('t[s]')
plt.ylabel('Temperature in degC')
plt.grid()

#This starts to log the temperature data from the DAQ device
def logging(i, yaxis):
    value = read_daq()
    print("Temperature =", round(value,1), "[degC]")
    data.append(value) #Adding to our array 
    time.sleep(sampling_time) #Adding to this array
    global k
    k += 1
    writeFileData(k*sampling_time, value)
    yaxis.append(value) #Adding to y list, but must limit(next line)
    yaxis = yaxis[-length_x:]
    line.set_ydata(yaxis) #Updating line with new values
    return line, 
ani = animation.FuncAnimation(figure,
    logging,
    fargs=(yaxis,),
    interval = 100,
    blit = True)
plt.show()