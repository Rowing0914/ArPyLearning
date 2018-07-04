"""
official doc: using AJAX on Flask  
http://flask.pocoo.org/docs/1.0/patterns/jquery/
"""

from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
    return render_template('temp.html')

if __name__ == '__main__':
	app.run(port=5050)