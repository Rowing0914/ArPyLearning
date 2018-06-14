import serial
import time
from Arduino import Arduino

board = Arduino('9600', port='/dev/cu.usbmodem14111')

no_servo = 9
board.Servos.attach(no_servo) #declare servo on pin no_servo
board.Servos.write(no_servo, 180) #move servo on pin no_servo to 0 degrees
print board.Servos.read(no_servo) # should be 0
time.sleep(0.01)
board.Servos.detach(no_servo) #free pin no_servo