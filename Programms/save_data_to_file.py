from datetime import datetime 
import time
import serial

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

while True:
    data = arduino.readline().decode().strip()

    if data:
        current_time = datetime.now().strftime("%m-%d %H:%M")
        
        with open("/home/arduinoproject/Documents/pythonws/Arduino-combined-with-Pandas/Programms/temperature.txt", "a") as file:
            file.write(data + ", " + current_time + "\n")
            print(data)
            file.flush()
