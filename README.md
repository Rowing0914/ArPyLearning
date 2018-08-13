# ArPyLearning

ArPyLearning is a light-weight Python library for
communicating with [Arduino microcontroller boards](http://www.arduino.cc/) from a connected computer using
standard serial IO, either over a physical wire 
or wirelessly. It is written using a custom protocol, similar to [Firmata](http://firmata.org/wiki/Main_Page).

Basically this project is hugely inspired by the great repo below.  
[**Python-Arduino-Command-API**](https://github.com/thearn/Python-Arduino-Command-API)
So please do not forget to check this out as well! Your star will be appreciated!

This allows a user to have an easy prototyping in dev and a maintainance of the connectivity with some webframework like Flask.

# Deep Reinforcement Learning
## DQN(Deep Q Network)
- check the code inside `./DRL/src/app.py`
- Agent is defined in DQN.py

# Arduino Control
## Simple usage example (LED blink)
```python
#!/usr/bin/env python
"""
 Blinks an LED on digital pin 13
 in 1 second intervals
"""

from Arduino import Arduino
import time

board = Arduino('9600') #plugged in via USB, serial com at rate 9600
board.pinMode(13, "OUTPUT")

while True:
    board.digitalWrite(13, "LOW")
    time.sleep(1)
    board.digitalWrite(13, "HIGH")
    time.sleep(1)
```

## Requirements:
- [Python](http://python.org/) 2.3 or higher
- Python 3.x is supported as well
- [pyserial](http://pyserial.sourceforge.net/) 2.6 or higher
- Any [Arduino compatible microcontroller](https://www.sparkfun.com/categories/242) with at least **14KB** of flash memory



## To-do list:
1. Check examples.py and setup.py again in example directory
2. finish implementing the DQN or some Deep Reinforcement Learning methods

