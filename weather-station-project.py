#Todo
#Reads directory for a file of a certain name to make sure it doesnt log on an existing file
import serial
import numpy as np
import datetime
import csv

fileName = input("Enter a name for the file to be created and press Enter: ")

ser = serial.Serial('COM4', baudrate = 9600, timeout=1)

firstTime = True    

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
            
            with open("%s.csv" % (fileName), "a", newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=",")
                
                if firstTime == True:
                    writer.writerow(["Time HH:MM:SS", "Humidity %", "Temperature_h F",
                                     "Pressure Pa", "Temperature_p F",
                                     "Light V", "Battery V"])
                    firstTime = False
                    
                writer.writerow(["%s:%s:%s" % (currentTime.hour, currentTime.minute,
                                                  currentTime.second), dataArray[0], dataArray[1],
                                                  dataArray[2], dataArray[3],
                                                  dataArray[4], dataArray[5]])
        
    except: #Ctrl-C to interrupt
        ser.close()
        print("Keyboard interrupt")
        break