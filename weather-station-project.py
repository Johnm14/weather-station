import serial
from time import time

ser = serial.Serial('COM4', baudrate = 9600, timeout=1)
    
while True:
    try:
        arduinoData = ser.readline()
        print(arduinoData)
    except: #Ctrl-C to interrupt
        ser.close()
        print("Keyboard interrupt")
        break