#!/usr/bin/env python
     
# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!
     
import RPi.GPIO as GPIO, time, os
import time
    
DEBUG = 1

def blink(numTimes,speed):
     GPIO.setmode(GPIO.BOARD)
     GPIO.setup(7,GPIO.OUT)
     GPIO.setup(16,GPIO.OUT)
     GPIO.setup(13,GPIO.OUT)
     p=GPIO.PWM(13,50)
     p.start(7.5)
     for t in range (0,1):

     for i in range (0,numTimes):
          print "Blink Eyes " + str(i+1)
          GPIO.output(7,True)
          GPIO.output(16,True)
          p.ChangeDutyCycle(7.5)
          time.sleep(speed)
          GPIO.output(7,False)
          GPIO.output(16,False)
          p.ChangeDutyCycle(12.5)
          time.sleep(speed)
     GPIO.cleanup()
     p.stop()

def photocell (PCpin):
     reading = 0
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(PCpin, GPIO.OUT)
     GPIO.output(PCpin, GPIO.LOW)
     time.sleep(0.1)
     GPIO.setup(PCpin, GPIO.IN)
     # This takes about 1 millisecond per loop cycle
     while (GPIO.input(PCpin) == GPIO.LOW):
          reading += 1
     return reading

def servo ():
     GPIO.setmode(GPIO.BOARD)
     GPIO.setup(13,GPIO.OUT)
     print "Start Servo"
     p = GPIO.PWM(13,50)
     p.start(7.5)
     p.ChangeDutyCycle(7.5)
     time.sleep(1)
     p.ChangeDutyCycle(12.5)
     time.sleep(1)
     p.ChangeDutyCycle(2.5)
     time.sleep(1)
     p.stop()

print "Animatroic Skull \n\n"

while True:     
     if photocell(18) > 400:
          blink(10,1)
	  #servo()
