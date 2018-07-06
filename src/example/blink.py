import time
from pyfirmata import Arduino, util

board = Arduino('/dev/cu.usbmodem14311')

def Blink(board, pin, signal):
	board.digital[pin].write(signal)

def distance_sensor(board, pin):
	board.analog[1].enable_reporting()
	return board.analog[1].read()

if __name__ == '__main__':
	it = util.Iterator(board)
	it.start()
	board.analog[1].enable_reporting()
	while True:
		Blink(board, 13, 1)
		time.sleep(0.05)
		Blink(board, 13, 0)
		time.sleep(0.05)
		print(distance_sensor(board, 1))