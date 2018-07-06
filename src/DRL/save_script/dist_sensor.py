#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Created by yubi

import serial
import time

ser = serial.Serial(port='/dev/cu.usbmodem14311',baudrate=9600)
def get_distance():
	while ser.inWaiting() == 0:
		time.sleep(0.05)
	
	val = int(ser.readline())
	val = 0   if val < 0   else val
	val = 100 if val > 100 else val
	return val

if __name__ == '__main__':
	while True:
		print(get_distance())