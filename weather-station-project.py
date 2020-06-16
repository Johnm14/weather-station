import serial
import numpy as np

ser = serial.Serial('COM4', baudrate = 9600, timeout=1)
#ser.reset_input_buffer() #might be needed
    
while True:
    try:
        arduinoData = ser.readline()
        dataStr = arduinoData.decode("utf-8")
        strippedString = dataStr.rstrip()
        dataList = strippedString.split(",")
        if len(dataList) == 6: #add an else statement to print what data i did get
            humidity = dataList[0]
            temperature1 = dataList[1]
            pressure = dataList[2]
            temperature2 = dataList[3]
            light = dataList[4]
            print(humidity)
            print(temperature1)
            print(pressure)
            print(temperature2)
            print(light)
            print('\n')
            
        #dataArray_str = np.array(dataList)
        #dataArray = np.fromstring(dataArray_str, dtype = np.float, sep = ', ')
        #dataArray = dataArray_str.astype(float)
        
        
        #humidity = dataArray_str[0]
        #temperature1 = dataArray_str[1]
        #pressure = dataArray_str[2]
        #temperature2 = dataArray_str[3]
        #light = dataArray_str[4]
        #voltage = dataArray_str[5]
        
        #print(humidity)
        #print(temperature1)
        #print(pressure)
        #print(temperature2)
        #print(light)
       # print(dataArray_str)
    except: #Ctrl-C to interrupt
        ser.close()
        print("Keyboard interrupt")
        break
'''while True:
    arduinoData = ser.readline()
    dataStr = arduinoData.decode("utf-8")
    strippedString = dataStr.rstrip()
    dataList = strippedString.split(",")
    if len(dataList) == 6:
        humidity = dataList[0]
        temperature1 = dataList[1]
        print(humidity)
        print(temperature1)
    #dataArray_str = np.array(dataList)
        #dataArray = np.fromstring(dataArray_str, dtype = np.float, sep = ', ')
    #print(dataList)
    #humidity = dataList[0]
    #temperature1 = dataList[1]
    #print(humidity)
    #print(temperature1)

    #print(dataArray_str)'''