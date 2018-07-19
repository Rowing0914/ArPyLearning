import serial
import time
from pyfirmata import Arduino, util

class Robot:
	def __init__(self, board):
		self.L1 = 11
		self.L2 = 10
		self.R1 = 6
		self.R2 = 5
		self.board = board

	def move_forward(self):
		self.board.digital[self.L1].write(1)
		self.board.digital[self.L2].write(0)
		self.board.digital[self.R1].write(1)
		self.board.digital[self.R2].write(0)

	def move_backward(self):
		self.board.digital[self.L1].write(0)
		self.board.digital[self.L2].write(1)
		self.board.digital[self.R1].write(0)
		self.board.digital[self.R2].write(1)

	def stop(self):
		self.board.digital[self.L1].write(0)
		self.board.digital[self.L2].write(0)
		self.board.digital[self.R1].write(0)
		self.board.digital[self.R2].write(0)

if __name__ == '__main__':
	board = Arduino('/dev/cu.usbmodem14111')
	# board = Arduino('/dev/cu.wchusbserial14110')
	robot = Robot()
	actions = ['f', 'b', 's']

	for a in actions:
		if a == 's':
			print("stop")
			robot.stop()
		elif a == 'b':
			print("go_backward")
			robot.move_backward()
			time.sleep(1)
		elif a == 'f':
			print("go_forward")
			robot.move_forward()
			time.sleep(1)