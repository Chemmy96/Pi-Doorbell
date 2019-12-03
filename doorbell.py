#!/usr/bin/python
import time
import subprocess
import RPi.GPIO as GPIO
import datetime as dt
import math

now = dt.datetime.today()
winter_sound = "/home/pi/doorbell/christmas.wav"
evening_sound = "/home/pi/doorbell/m_gaye.wav"
spring_sound = "/home/pi/doorbell/spring.wav"
summer_sound = "/home/pi/doorbell/summer.wav"
fall_sound = "/home/pi/doorbell/september.wav"

Q=math.ceil(now.month/3.)

def play_sound():
    if 4 > now.hour > 16:
        subprocess.call(["aplay", evening_sound])
    else:
        if Q==4:
            subprocess.call(["aplay", winter_sound])
        elif Q==1:
            subprocess.call(["aplay", spring_sound])
        elif Q==2:
            subprocess.call(["aplay", summer_sound])
        elif Q==3:
            subprocess.call(["aplay", fall_sound])


GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN)

try:
    while True:
         button_state = GPIO.input(22)
         if button_state == False:
             play_sound()
             time.sleep(5)
except:
    GPIO.cleanup()
