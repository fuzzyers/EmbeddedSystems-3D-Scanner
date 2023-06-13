import smbus
import time
import picamera
import os
from time import sleep
from datetime import date

camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()
bus = smbus.SMBus(1)
arduino_address = 0x12
value_to_send = 0
data_received = 0

folder_name = date.today().strftime("%d-%m-%Y")
folder_path = '../pictures/' + folder_name
os.mkdir(folder_path, exsist_ok=True)

# Define states
STATE_IDLE = 0
STATE_MOTOR_TURN = 1
STATE_TAKE_PHOTO = 2

# Initialize current state
current_state = STATE_IDLE

def motorturn():
    global current_state, data_received

    if current_state == STATE_MOTOR_TURN:
        bus.write_byte(arduino_address, value_to_send)
        data_received = bus.read_byte(arduino_address)
        current_state = STATE_TAKE_PHOTO

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
