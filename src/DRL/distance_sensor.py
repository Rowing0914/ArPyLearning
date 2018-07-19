import time
from pyfirmata import Arduino, util

class Sensor:
	def __init__(self, board, pin=1):
		self.board = board
		self.pin = pin
		self.board.analog[self.pin].enable_reporting()
		it = util.Iterator(self.board)
		it.start()

	def get_distance(self):
		self.board.analog[self.pin].enable_reporting()
		return self.board.analog[self.pin].read()

if __name__ == '__main__':
	board = Arduino('/dev/cu.usbmodem14111')
	sensor = Sensor(board, pin=1)
	while True:
		# output range is [1,0]
		print(sensor.get_distance())