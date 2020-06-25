#Todo
#Reads directory for a file of a certain name to make sure it doesnt log on an existing file
import serial
import numpy as np
import datetime
import csv

ser = serial.Serial('COM4', baudrate = 9600, timeout=1)
    
while True:
    try:
        arduinoData = ser.readline()
        dataStr = arduinoData.decode("utf-8")
        strippedString = dataStr.rstrip()
        dataList = strippedString.split(",")
        
        if len(dataList) == 6: #add an else statement to print what data i did get?
            
            dataArray_str = np.array(dataList)
            dataArray = dataArray_str.astype(float)
            
            currentTime = datetime.datetime.now()
            
            print(dataArray)
            print("%s:%s:%s" % (currentTime.hour, currentTime.minute, currentTime.second))
            
            with open("%s_%s.csv" % (currentTime.month, currentTime.day), "a", newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=",")
                
                writer.writerow(["%s:%s:%s" % (currentTime.hour, currentTime.minute,
                                                  currentTime.second), dataArray[0], dataArray[1],
                                                  dataArray[2], dataArray[3],
                                                  dataArray[4], dataArray[5]])
        
    except: #Ctrl-C to interrupt
        ser.close()
        print("Keyboard interrupt")
        break