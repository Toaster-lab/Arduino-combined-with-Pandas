#Saving data I got from Serial to a txt file
import serial

#Functions:
arduino = serial.Serial("COM4", 9600)

data = arduino.readline()

with open("tempature", "w") as file:
    file.write(data, "\n")
