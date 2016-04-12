#!/usr/bin/env python

import max7219.led as led
from time import sleep

device = led.matrix(2)
device.orientation(270)
device.brightness(0)

for x in range(600):
	device.letter(0,0x03)
	device.letter(1,0x03)
	device.letter(0 + (x % 2),0x00)
	sleep(0.01)
	list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	device.brightness(list[x % 30])
device.clear()
