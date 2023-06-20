#Run this to install library pip install RPi.GPIO
import RPi.GPIO as GPIO
import time
import subprocess
import ctypes

GPIO.setmode(GPIO.BCM)
button_pin = 14
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
button_pin = 14
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

is_script_running = False

def run_script(channel):
    global is_script_running

    if not is_script_running:
        is_script_running = True
        subprocess.call("python ./python-i2c.py", shell=True)
        is_script_running = False

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=run_script, bouncetime=200)

while True:
    time.sleep(1)
