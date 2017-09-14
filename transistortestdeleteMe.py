# Reading from the MCP3008 and stroing the date
# Execute me with: sudo python readAndStoreSensorData.py
import time
from time import sleep,localtime, strftime
import sys
import numpy as np
import os

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

import RPi.GPIO as GPIO #For pulling pins high/low

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

pinOnOff=20
GPIO.setup(pinOnOff, GPIO.OUT)
GPIO.output(pinOnOff, GPIO.HIGH)
print("On")
samplingTime=5; # time through which sensor data is sampled
time.sleep(samplingTime)
print("OFF")
GPIO.output(pinOnOff, GPIO.LOW)

