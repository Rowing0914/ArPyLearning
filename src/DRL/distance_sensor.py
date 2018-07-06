import time
from pyfirmata import Arduino, util

pin = 1
board = Arduino('/dev/cu.usbmodem14311')
board.analog[pin].enable_reporting()
it = util.Iterator(board)
it.start()

def get_distance(pin):
	board.analog[pin].enable_reporting()
	print("from dist:", board.analog[pin].read())
	return board.analog[pin].read()

if __name__ == '__main__':
	while True:
		# output range is [1,0]
		print(get_distance(pin))