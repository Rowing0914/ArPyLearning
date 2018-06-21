#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Usage : 
# from dist_sensor import get_distance
# a = get_distance()
# This function returns the distance in terms of value between 0.0 - 1.0
# near 0.0 value means it is too far from sensor
# near 1.0 value means quite close to sensor
# Author : Yoovraj Shinde
# Email  : yashinde@gmail.com

import serial
import time


def get_distance(port='/dev/ttyUSB0', baudrate=9600):
   ser = serial.Serial(port=port,baudrate=baudrate)

   ser.write(b'r')
   val = ""
   time.sleep(0.05)
   while ser.inWaiting():
      val = int(ser.readline())
   val = 0   if val < 0   else val
   val = 100 if val > 100 else val
   # val = val / 100.0
   return val

