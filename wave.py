#!/usr/bin/env python

import max7219.led as led
from time import sleep

device = led.matrix(2)
device.orientation(270)
device.brightness(0)

time = 0.01
count = 5

for x in range(8):
    for y in range(8):
	device.pixel(x,y,1)
	sleep(time)

for i in range(count):
    for x in range(8):
        for y in range(8):
    	    device.pixel(x,y,0)
       	    device.pixel(8 + x,y,1)
       	    sleep(time)
    for x in range(8):
        for y in range(8):
	    device.pixel(8 + x,y,0)	
	    device.pixel(x,y,1)
	    sleep(time)

for x in range(8):
    for y in range(8):
        device.pixel(x,y,0)
        device.pixel(8 + x,y,1)
	sleep(time)

for x in range(8):
    for y in range(8):
        device.pixel(8 + x,y,0)
        sleep(time)
