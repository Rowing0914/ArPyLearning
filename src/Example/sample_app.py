from ArPyLearning import Arduino
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world():
	print('hello_world')
	return 'Hello, World!'

@app.route('/blink')
def blink():
	return render_template('index.html')

@app.route('/low')
def Blink_low():
	board.digitalWrite(led_pin, "LOW")

@app.route('/high')
def Blink_high():
	board.digitalWrite(led_pin, "HIGH")

if __name__ == '__main__':
	led_pin = 13
	baud = 9600
	port = "your port"

	# initialise the board
	# board = Arduino(baud, port=port)
	# board.pinMode(led_pin, "OUTPUT")
	# app.run(host='0.0.0.0', port=5000)
	app.run(port=5000)