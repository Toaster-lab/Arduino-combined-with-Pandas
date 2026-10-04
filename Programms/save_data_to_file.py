
import serial
from datetime import datetime 
import time

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

with open("/home/arduinoproject/Documents/pythonws/Arduino-combined-with-Pandas/Programms/temperature.txt", "w") as file:

    while True:
       data = arduino.readline().decode().strip()

       if data:
           current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           file.write(data + ", " + current_time + "\n")
    
           file.flush()
       time.sleep(3600)

