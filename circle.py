#!/usr/bin/env python

import max7219.led as led
from time import sleep

device = led.matrix(2)
device.orientation(270)
device.brightness(0)

time = 0.01

for y in range(8):
    device.pixel(0, y, 1)
    sleep(time)
for x in range(15):
    device.pixel(1+x, 7, 1)
    sleep(time)
for y in range(7):
    device.pixel(15, 6-y , 1)
    sleep(time)
for x in range(14):
    device.pixel(14-x, 0, 1)
    sleep(time)

for y in range(6):
    device.pixel(1, 1+y, 1)
    sleep(time)
for x in range(13):
    device.pixel(2+x, 6, 1)
    sleep(time)
for y in range(5):
    device.pixel(14, 5-y , 1)
    sleep(time)
for x in range(12):
    device.pixel(13-x, 1, 1)
    sleep(time)

for y in range(4):
    device.pixel(2, 2+y, 1)
    sleep(time)
for x in range(11):
    device.pixel(3+x, 5, 1)
    sleep(time)
for y in range(3):
    device.pixel(13, 4-y , 1)
    sleep(time)
for x in range(10):
    device.pixel(12-x, 2, 1)
    sleep(time)

for y in range(2):
    device.pixel(3, 3+y, 1)
    sleep(time)
for x in range(9):
    device.pixel(4+x, 4, 1)
    sleep(time)
for x in range(9):
    device.pixel(12-x, 3, 1)
    sleep(time)

for y in range(8):
    device.pixel(0, y, 0)
    sleep(time)
for x in range(15):
    device.pixel(1+x, 7, 0)
    sleep(time)
for y in range(7):
    device.pixel(15, 6-y , 0)
    sleep(time)
for x in range(14):
    device.pixel(14-x, 0, 0)
    sleep(time)

for y in range(6):
    device.pixel(1, 1+y, 0)
    sleep(time)
for x in range(13):
    device.pixel(2+x, 6, 0)
    sleep(time)
for y in range(5):
    device.pixel(14, 5-y , 0)
    sleep(time)
for x in range(12):
    device.pixel(13-x, 1, 0)
    sleep(time)

for y in range(4):
    device.pixel(2, 2+y, 0)
    sleep(time)
for x in range(11):
    device.pixel(3+x, 5, 0)
    sleep(time)
for y in range(3):
    device.pixel(13, 4-y , 0)
    sleep(time)
for x in range(10):
    device.pixel(12-x, 2, 0)
    sleep(time)

for y in range(2):
    device.pixel(3, 3+y, 0)
    sleep(time)
for x in range(9):
    device.pixel(4+x, 4, 0)
    sleep(time)
for x in range(9):
    device.pixel(12-x, 3, 0)
    sleep(time)

