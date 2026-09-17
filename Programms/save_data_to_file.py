#Saving data I got from Serial to a txt file
import serial

#Functions:
arduino = serial.Serial("COM4", 9600)



with open("temperature.txt", "w") as file:
    while True:
       data = arduino.readline().decode().strip()
       file.write(data + "\n")
       #print(data) <= to check if it even recieves data
       file.flush()
#I am going to need to create a list with the data I get from Serial
#My data should be in a specific order so I can assign each column their respecting name.
