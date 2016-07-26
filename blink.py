#!/usr/bin/env python

import RPi.GPIO as GPIO, time, os
import time
import pygame

def skull():
     ###
     # Anamitronic Skull
     # Blinks the eyes, activates the servo, and plays a sound
     ###

     print "Anamitroic Skull Activated \n\n"

     playsound()
     blink (1,1)
     servo()
     blink (1,1)
     servo()
     blink (5,1)

def blink(numTimes,speed):
     GPIO.setmode(GPIO.BOARD)
     GPIO.setup(7,GPIO.OUT)
     GPIO.setup(16,GPIO.OUT)
     GPIO.setup(13,GPIO.OUT)
     for i in range (0,numTimes):
          print "Blink Eyes " + str(i+1)
          GPIO.output(7,True)
          GPIO.output(16,True)
          time.sleep(speed)
          GPIO.output(7,False)
          GPIO.output(16,False)
          time.sleep(speed)
     GPIO.cleanup()

def photocell (PCpin):
     ###
     # Reads the value of the photoresistor.
     ###
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
     ###
     # Activates the Servo to two different positions, neutral and 180
     # Commented out value would rotate back to 0
     ###
     GPIO.setmode(GPIO.BOARD)
     GPIO.setup(13,GPIO.OUT)
     print "Start Servo"
     p = GPIO.PWM(13,50)
     p.start(7.5)
     p.ChangeDutyCycle(7.5)
     time.sleep(1)
     p.ChangeDutyCycle(12.5)
     time.sleep(1)
     #p.ChangeDutyCycle(2.5)
     #time.sleep(1)
     p.stop()

def playsound ():
     ###
     # Plays sound from home folder
     ###
     print "Playing skull.wav"
     pygame.mixer.init()
     pygame.mixer.music.load("/home/pi/boo.wav")
     pygame.mixer.music.play()
     time.sleep(1)
     pygame.mixer.music.load("/home/pi/skull.wav")
     pygame.mixer.music.play()

blink(1,1)
blink(1,1)
blink(1,1)
blink(1,1)
blink(1,1)

