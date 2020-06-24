import serial
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime

ser = serial.Serial('COM4', baudrate = 9600, timeout=1)
#ser.reset_input_buffer() #might be needed
    
while True:
    try:
        arduinoData = ser.readline()
        dataStr = arduinoData.decode("utf-8")
        strippedString = dataStr.rstrip()
        dataList = strippedString.split(",")
        
        if len(dataList) == 6: #add an else statement to print what data i did get
            '''humidity = dataList[0]
            temperature1 = dataList[1]
            pressure = dataList[2]
            temperature2 = dataList[3]
            light = dataList[4]'''
            
            dataArray_str = np.array(dataList)
            dataArray = dataArray_str.astype(float)
            
            currentTime = datetime.datetime.now()
            #time = matplotlib.dates.date2num(currentTime) #can we even use this float generated here?
            
            #plt.plot(time, dataArray[0])
            
            print(dataArray)
            print("%s:%s:%s" % (currentTime.hour, currentTime.minute, currentTime.second))
        
    except: #Ctrl-C to interrupt
        ser.close()
        print("Keyboard interrupt")
        break