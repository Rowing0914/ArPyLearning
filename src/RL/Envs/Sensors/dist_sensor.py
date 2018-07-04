#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Usage : pin is A1!!

# import serial
from serial import serial
import time

ser = serial.Serial(port='/dev/cu.usbmodem14311',baudrate=9600)
def get_distance():
   while ser.inWaiting() == 0:
      time.sleep(0.05)
   val = int(ser.readline())
   val = 0   if val < 0   else val
   val = 100 if val > 100 else val
   # val = val / 100.0
   return val

def _get_distance():
	return 'h'

if __name__ == '__main__':
   while True:
      print(get_distance())