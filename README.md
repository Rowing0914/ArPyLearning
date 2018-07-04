# ArPyLearning

ArPyLearning is a light-weight Python library for
communicating with [Arduino microcontroller boards](http://www.arduino.cc/) from a connected computer using
standard serial IO, either over a physical wire 
or wirelessly. It is written using a custom protocol, similar to [Firmata](http://firmata.org/wiki/Main_Page).

Basically this project is hugely inspired by the great repo below.  
[**Python-Arduino-Command-API**](https://github.com/thearn/Python-Arduino-Command-API)
So please do not forget to check this out as well! Your star will be appreciated!

This allows a user to have an easy prototyping in dev and a maintainance of the connectivity with some webframework like Flask.

# Usage
- Navigate to `skeches/prototype` and open the `prototype.ino` on Arduino IDE
- Confirm it and load it to your Arduino

# Python Version
We have tested the modules with 3.6.x

# Package Structure
- docs: Maintenance Document Purpose , we are using Sphinx for documenting
- publish: Document Storage, feel free to refer to `index.html`
- skeches: Containing the core wrapper for Arduino
- src: Containing the python wrapper of the skeches in Arduino

# Basic Maintenance Rule
- update the docs: `bash update_docs.sh`
- create the docs: `bash gen_docs.sh`

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

## Installation:
<font color='red'>TO-DO: we have to confirm the procedure to install</font>  
Either run `pip install arduino-python` from a command line, or run `python setup.py
build install` from the source directory to install this library.

## Setup:
1. <font color='red'>**Verify**</font> that your Arduino board communicates at the baud rate specified in the
`setup()` function (line 348) in `prototype.ino`. Change it there if necessary.
2. <font color='red'>**Load**</font> the `prototype.ino` sketch onto your Arduino board, using the Arduino IDE.
3. <font color='red'>**Test**</font> connect your Arduino board and your computer and try this example python scripts `examples.py`

## Testing:
The `tests` directory contains some basic tests for the library. Extensive code coverage is a bit difficult to expect for every release, since a positive test involves actually
connecting and issuing commands to a live Arduino, hosting any hardware
required to test a particular function. But a core of basic communication tests
should at least be maintained here and used before merging into the `master` branch.

After installation, the interactive tests can be run from the source directory:
```bash
$ python tests/test_main.py
```

Automated tests can be run from the source directory with:
```bash
$ python tests/test_arduino.py
```

## Classes
- `Arduino(baud)` - Set up communication with currently connected and powered
Arduino.

```python
board = Arduino("9600") #Example
```

The device name / COM port of the connected Arduino will be auto-detected.
If there are more than one Arduino boards connected,
the desired COM port can be also be passed as an optional argument:

```python
board = Arduino("9600", port="COM3") #Windows example
```
```python
board = Arduino("9600", port="/dev/tty.usbmodemfa141") #OSX example
```

A time-out for reading from the Arduino can also be specified as an optional
argument:

```python
board = Arduino("9600", timeout=2) #Serial reading functions will
#wait for no more than 2 seconds
```

## Methods

**Digital I/O**

- `Arduino.digitalWrite(pin_number, state)` turn digital pin on/off
- `Arduino.digitalRead(pin_number)` read state of a digital pin

```python
#Digital read / write example
board.digitalWrite(13, "HIGH") #Set digital pin 13 voltage
state_1 = board.digitalRead(13) #Will return integer 1
board.digitalWrite(13, "LOW") #Set digital pin 13 voltage
state_2 = board.digitalRead(13) #Will return integer 0
```

- `Arduino.pinMode(pin_number, io_mode)` set pin I/O mode
- `Arduino.pulseIn(pin_number, state)` measures a pulse
- `Arduino.pulseIn_set(pin_number, state)` measures a pulse, with preconditioning

```python
#Digital mode / pulse example
board.pinMode(7, "INPUT") #Set digital pin 7 mode to INPUT
duration = board.pulseIn(7, "HIGH") #Return pulse width measurement on pin 7
```

**Analog I/O**

- `Arduino.analogRead(pin_number)` returns the analog value
- `Arduino.analogWrite(pin_number, value)` sets the analog value

```python
#Analog I/O examples
val=board.analogRead(5) #Read value on analog pin 5 (integer 0 to 1023)
val = val / 4 # scale to 0 - 255
board.analogWrite(11) #Set analog value (PWM) based on analog measurement
```

**Shift Register**

- `Arduino.shiftIn(dataPin, clockPin, bitOrder)` shift a byte in and returns it
- `Arduino.shiftOut(dataPin, clockPin, bitOrder, value)` shift the given byte out

`bitOrder` should be either `"MSBFIRST"` or `"LSBFIRST"`

**Servo Library Functionality**
Support is included for up to 8 servos.

- `Arduino.Servos.attach(pin, min=544, max=2400)` Create servo instance. Only 8 servos can be used at one time.
- `Arduino.Servos.read(pin)` Returns the angle of the servo attached to the specified pin
- `Arduino.Servos.write(pin, angle)` Move an attached servo on a pin to a specified angle
- `Arduino.Servos.writeMicroseconds(pin, uS)` Write a value in microseconds to the servo on a specified pin
- `Arduino.Servos.detach(pin)` Detaches the servo on the specified pin

```python
#Servo example
board.Servos.attach(9) #declare servo on pin 9
board.Servos.write(9, 0) #move servo on pin 9 to 0 degrees
print board.Servos.read(9) # should be 0
board.Servos.detach(9) #free pin 9
```

**Software Serial Functionality**

- `Arduino.SoftwareSerial.begin(ss_rxPin, ss_txPin, ss_device_baud)` initialize software serial device on
specified pins.
Only one sofware serial device can be used at a time. Existing software serial instance will
be be overwritten by calling this method, both in Python and on the arduino board.
- `Arduino.SoftwareSerial.write(data)` send data using the arduino 'write' function to the existing software
serial connection.
- `Arduino.SoftwareSerial.read()` returns one byte from the existing software serial connection

```python
#Software serial example
board.SoftwareSerial.begin(0, 7, "19200") # Start software serial for transmit only (tx on pin 7)
board.SoftwareSerial.write(" test ") #Send some data
response_char = board.SoftwareSerial.read() #read response character
```

**EEPROM**

- `Arduino.EEPROM.read(address)` reads a byte from the EEPROM
- `Arduino.EEPROM.write(address, value)` writes a byte to the EEPROM
- `Arduino.EEPROM.size()` returns size of the EEPROM

```python
#EEPROM read and write examples
location = 42
value = 10 # 0-255(byte)

board.EEPROM.write(location, 10) 
print(board.EEPROM.read(location))
print('EEPROM size {size}'.format(size=board.EEPROM.size()))
```

**Misc**

- `Arduino.close()` closes serial connection to the Arduino.
