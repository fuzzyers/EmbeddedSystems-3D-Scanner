#Run this to install library pip install RPi.GPIO
import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
button_pin = #unassigned currently
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def run_script():
    subprocess.call("script command", shell=True)

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=run_script, bouncetime=200)

while True:
    time.sleep(1)