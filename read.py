#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import datetime

while True:
    
    reader = SimpleMFRC522.SimpleMFRC522()
    try:
        id, text = reader.read()
        print(id)
        print(text)
    finally:
        GPIO.cleanup()
        print('done')
        print( datetime.datetime.now())
