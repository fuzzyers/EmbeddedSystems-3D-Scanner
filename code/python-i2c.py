# @file: python-i2c.py
# @brief: Python script to control the Arduino via I2C
# @details: This script is used to control the Arduino via I2C.
# It sends a value to the Arduino, which then turns the motor.
# After the motor has turned, the Arduino sends a value back to the Raspberry Pi.
# When the Raspberry Pi receives the value, it takes a photo and saves it to the pictures folder.
# The pictures folder is named after the current date.
# The pictures are named after the current time.
# The pictures folder is located in the parent directory of the current directory.
# The pictures folder is created if it doesn't exist.
# @author: Jackson Williamson
# @date: 13/06/2023
import smbus
import time
import picamera
import os
from time import sleep
from datetime import date

# Initialize camera
camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()

# Initialize I2C
bus = smbus.SMBus(1)
arduino_address = 0x12
value_to_send = 0
data_received = 0

# Define folder path
folder_name = date.today().strftime("%d-%m-%Y")
folder_path = '../pictures/' + folder_name
# Create folder if it doesn't exist
os.mkdir(folder_path, exist_ok=True)

# Define states
STATE_IDLE = 0
STATE_MOTOR_TURN = 1
STATE_TAKE_PHOTO = 2

# Initialize current state
current_state = STATE_IDLE

# Function motorturn sends a value to the Arduino, which then turns the motor.
# After the motor has turned, the Arduino sends a value back to the Raspberry Pi.
def motorturn():
    global current_state, data_received

    if current_state == STATE_MOTOR_TURN:
        bus.write_byte(arduino_address, value_to_send)
        data_received = bus.read_byte(arduino_address)
        current_state = STATE_TAKE_PHOTO

# Function takephoto takes a photo and saves it to the pictures folder.
# The pictures folder is named after the current date.
def takephoto():
    global current_state, data_received

    if current_state == STATE_TAKE_PHOTO and data_received == 0:
        sleep(10)
        file_name = "photo_" + str(int(time.time())) + ".jpg"
        file_path = os.path.join(folder_path, file_name)
        camera.capture(file_path)   
        current_state = STATE_IDLE

while True:
    if current_state == STATE_IDLE:
        value_to_send = 1
        current_state = STATE_MOTOR_TURN

    motorturn()
    takephoto()
