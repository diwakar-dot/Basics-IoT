
#with this code you are able to read data from arduino serial monitor.The data can be saved in your pc as a csv file
#we can have a scatterplot for the data stored in .




#pre-requisites
#ensure that your laptop is connected to arduino with sensors and required hardware components.
#download pyserial,matplotlib packages in case if you dont have.


import serial; 				#importing pyserial package
import time;				#importing time 
import csv;
import matplotlib.pyplot as plt		#importing matplotlib packages
ser=serial.Serial("/dev/ttyUSB0",9600)  #"/dev/ttyUSB0" is a port you are working with.
time.sleep(1)
data=[]
td=[]
n=input("enter no.of read")   # it needs no.of readings to be readed into a file in your computer

for i in range(n):
	b=ser.readline()
	stn=b.decode()
	st=stn.rstrip()
	flt=int(st)
print ("Distance:",flt)
	data.append(flt)
	time.sleep(0.1)
ser.close()

#for line in data:
	#print("Distance:",line)

with open("readings.csv",'w+') as csvfile:			#this will create a csv file named:readings
								
filewriter=csv.writer(csvfile,delimiter=',')
for i in range(n):
	t=time.localtime()
	d=time.strftime("%H:%M,%s",t)
	td.append(d)
	filewriter.writerow([d,flt])

plt.scatter(data,td)
					#plotting a graph
					#also you can plot a bargraph,boxplot by changing commands.
plt.title('distance vs time')
plt.xlabel("distance")
plt.ylabel("time")
plt.show()







