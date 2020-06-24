import serial
import numpy as np
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
            
            dataArray_str = np.array(dataList)
            dataArray = dataArray_str.astype(float)
            
            currentTime = datetime.datetime.now()
            
            print(dataArray)
            print("%s:%s:%s" % (currentTime.hour, currentTime.minute, currentTime.second))
        
    except: #Ctrl-C to interrupt
        ser.close()
        print("Keyboard interrupt")
        break