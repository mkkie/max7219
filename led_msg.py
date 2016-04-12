#!/usr/bin/env python

import sys
import max7219.led as led
from time import sleep
import getopt

bright_number = 0
message = ""

opts, args = getopt.getopt(sys.argv[1:], 'm:b:', ['message=', 'brightness=']) 
for opt, arg in opts:
    if opt in ('-b', '--brightness'):
	bright_number = arg
    elif opt in ('-m', '--message'):
	message = arg
    else:
	usage()
	sys.exit(2)

def usage():
    print '--brightness, --message'

def main():
    try:
	device = led.matrix(2)
	device.orientation(270)
	device.brightness(int(bright_number))
	if len(sys.argv) < 2:
	    sys.exit(1)
	else:
	    device.show_message(message)
    except KeyboardInterrupt:
	device.clear()

if __name__ == "__main__":
	main()
