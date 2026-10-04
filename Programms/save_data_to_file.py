
import serial
from datetime import datetime 

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

with open("/home/arduinoproject/Documents/pythonws/Arduino-combined-with-Pandas/Programms/temperature.txt", "w") as file:

    while True:
       data = arduino.readline().decode().strip()
       if data:
           time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Updates every loop
           
           file.write(data + ", " + time + "\n")
    
           file.flush()

