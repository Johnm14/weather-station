import serial
from time import time

ser = serial.Serial('COM4', baudrate = 9600, timeout=1)

#for closing the port, port must be closed after each run or the next run wont have permission
#ser.close()

end = time() + 60

while time() < end:
    arduinoData = ser.readline()
    print(arduinoData)

ser.close()

'''while 1:
    arduinoData = ser.readline()
    print(arduinoData)'''