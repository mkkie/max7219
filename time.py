#!/usr/bin/env python

import max7219.led as led
import time
import datetime

def main():
    try:
	device = led.matrix(2)
	device.orientation(270)
	t = time.time()
	ctime = datetime.datetime.fromtimestamp(t).strftime('%H:%M')
	device.show_message(ctime)
	device.clear()
    except KeyboardInterrupt:
	device.clear()

if __name__ == "__main__":
	main()
