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
            '''print(humidity)
            print(temperature1)
            print(pressure)
            print(temperature2)
            print(light)
            print('\n')'''
            dataArray_str = np.array(dataList)
            dataArray = dataArray_str.astype(float)
            print(dataArray)
        
    except: #Ctrl-C to interrupt
        ser.close()
        print("Keyboard interrupt")
        break