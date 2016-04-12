#!/usr/bin/env python

import max7219.led as led
import time
import datetime
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

device = led.matrix(2)
device.orientation(270)
device.brightness(0)

device.letter(0,ord('E'))
device.letter(1,ord('R'))
time.sleep(3)

for x in range(256):
    device.letter(1, 32 + (x % 64))
    device.letter(0, x)
    time.sleep(0.1)
