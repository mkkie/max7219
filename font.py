#!/usr/bin/env python

import max7219.led as led
import time
import datetime
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

device = led.matrix(2)
device.orientation(270)
device.brightness(0)

device.show_message("Alternative font!", font=SINCLAIR_FONT)
