import smbus
import time
from picamera import Picamera
from time import sleep

camera.start_preview()
bus = smbus.SMBus(1) #smbus 1 is for raspberrypi model 3 and below

arduino_address = 0x12
value_to_send = 42

bus.write_byte(arduino_address, value_to_send)

data_received = bus.read_byte(arduino_address)
print("Data received from Arduino:", data_received)

while true:
    motorturn()
    takephoto()

def motorturn():
    if value_to_send == 1:
        bus.write_byte(arduino_address, value_to_send)
        data_received = bus.read_byte(arduino_address)



def takephoto():
    if data_received == 0:
        sleep(10)
        camera.capture('../pictures/1/')
        #click
