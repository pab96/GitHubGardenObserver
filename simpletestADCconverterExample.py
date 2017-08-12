# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time
from time import gmtime, strftime
import sys
import numpy as np
import os

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

## Sensor data sampling
print('Reading MCP3008 values, press Ctrl-C to quit...')
samplingTime=2; # time through which sensor data is sampled
samplingInterval=0.25; # sample every 0.25sec
samplingCount=0
allSamplingValues=d = np.zeros((samplingTime/samplingInterval+1,8)) # Initialising a zeros matrix
while samplingCount<=samplingTime/samplingInterval:
    # Read all the ADC channel values in a list.
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        allSamplingValues[samplingCount][i]= mcp.read_adc(i)
    samplingCount += 1
    time.sleep(samplingInterval)

## Sensor data processing mean and std
averageSensorData=np.mean(allSamplingValues,axis=0)
stdSensorData=np.std(allSamplingValues,axis=0)
#print(allSamplingValues) # Print Raw values
#print("Averaged values:")
#print(averageSensorData)
#print(stdSensorData)
##sys.stdout.write(strftime("%d.%m.%Y %H:%M:%S", gmtime())) # use sys.stout.write to print in same line as command below
##print(' | {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*np.around(averageSensorData,decimals=1)))
##print(' | {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*np.around(stdSensorData,decimals=2)))

## preparing sensor data for storage
print("Date,Time | Avg_Sens_1 |Avg_Sens_2 |Avg_Sens_3 |Avg_Sens_4 |Avg_Sens_5 |Avg_Sens_6 |Avg_Sens_7 |Avg_Sens_8 |Std_Sens_1 |Std_Sens_2 |Std_Sens_3 |Std_Sens_4 |Std_Sens_5 |Std_Sens_6 |Std_Sens_7 |Std_Sens_8 |")
print('-' * 57)
sensorDataToBeSaved=strftime("%d.%m.%Y %H:%M:%S", gmtime()) # Date and Time
sensorDataToBeSaved += ' | {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4}'.format(*np.around(averageSensorData,decimals=1)) # The sensor data avaerage values to 1 decimal place
sensorDataToBeSaved += ' | {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4}'.format(*np.around(stdSensorData,decimals=2))    # The sensor data std values to 2 decimal place
print(sensorDataToBeSaved)

## Writing to Sensor Storage File
fileHandle=0;
if os.path.isfile("/home/pi/Desktop/TestPictures/GardenObserver_SensorData.txt"):  #check if file already exists
    fileHandle = open("/home/pi/Desktop/TestPictures/GardenObserver_SensorData.txt","a") #if already exist go to "a"= appendix mode and new text will be added below
    fileHandle.write("\n")
else:
    fileHandle = open("/home/pi/Desktop/TestPictures/GardenObserver_SensorData.txt","a")
    fileHandle.write("Date Time | Avg_Sens_1 |Avg_Sens_2 |Avg_Sens_3 |Avg_Sens_4 |Avg_Sens_5 |Avg_Sens_6 |Avg_Sens_7 |Avg_Sens_8 |Std_Sens_1 |Std_Sens_2 |Std_Sens_3 |Std_Sens_4 |Std_Sens_5 |Std_Sens_6 |Std_Sens_7 |Std_Sens_8 |") 
    fileHandle.write("\n")
    fileHandle.write('-' * 100)
    fileHandle.write("\n")

fileHandle.write(sensorDataToBeSaved)
fileHandle.close() 


