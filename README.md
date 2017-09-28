# GitHubGardenObserver
Documentation for "Remote Environment Controller for  Experiments in Extreme Environments"

# A Remote Environment Controller for Experiments in Extreme Environments




Solar Power and Batteries:

Using a timer:
Data recording is only required every hour or so. In the intervalls in between Pi can be switched off which saves a lot of power. Power consumption is cruicial in tis project if the Pi is powered by a battery and a solar panel. So the idea is that the Pi only swictehs on every hour read the sensors and then switch off gain. The sleep mode requires too much power, thus an external timer device is used. This timer is described here:
Some useful online resources on this:
- http://www.circuitbasics.com/555-timer-basics-astable-mode/ -> Simple way of building and testing the timer.
- http://www.ti.com/lit/ds/symlink/lm555.pdf -> 555 timer datasheet

The Pi 2B has 2 tiny pins labelled run. If these pins are briefly short circuted the Pi will restart. We will use these two pins to restart the Pi after it was shut down by simply connecting them to a transistor which is then switched by the 555 timer. The 555 timer needs to send a signal every hour for a very shor pulse. Thus the so called A-Stable-Mode is used. The Astable mode is such that it is on for most of the time and switches off for a shorter time. Therefore we have to invert this signal such that the two "Run" pins on the Pi are generally off and only swicth on every hour for a short pulse.
R_1, R_2 and C of the 555 timer determine how long the on and off time are given by:
t_on= 0.693*(R_1+R_2)*C
t_off=0.693*(R_2)*C
A one hour on time is quite long and we need big transistors and capacitors to do that. We chose:
R_1=5.1MOhm + 47kOhm +3.3KOhm= 5150.3kOhm
R_2=1kOhm
C=1000 uF
This results in:
t_on=3569.85s
t_off=0.69s 

![alt text](https://github.com/pab96/GitHubGardenObserver/blob/master/Data/GardenPiCam_20170812_182113.jpg "Picture Title")



Using the arduino pro mini
First install Arduino IDE. You can use an FTDI device to programm the mini. I tried wtih the one from sparkfun but no matter what I did my PC wouldnt recognice the driver. So I gave up and found a much better otion instead! You can programm the arduino pro mini with a normal Arduino Uno (the one where you can take out the ATMEGA328P), this worked first time I tried! So I recommend you use that option it also spares you from buying an FTDI, rather buy an arduino uno if you don't have one, I'm sure you'll find use for that later. 
Here (http://www.instructables.com/id/Program-Arduino-Pro-Mini-Using-Arduino-Uno/) is an excellent tutorial on how to programm the arduino pro mini using the arduino uno. In short you need to take out the ATMEGA328P from the Uno, then connect Uno ground to pro mini ground, the Uno 5V pin to VCC on the pro mini and the Rx and Tx pins as well as the reset pin from Uno to the pro mini. Then go to the Arduino IDE -> Tools-> Board -> Arduino Pro Mini  and make sure you have the corret port enabled. Then as usual just upload the program to the Uno which will then go to the pro mini and it works, MAGIC! (Sometimes still PC does not recognise port, try deplug usb with arduino and just uploading it several times at some stage it will work) 
Before you upload the program arduinoProMiniPowerTimer to the arduino you need to download the "LowPower.h" library (https://github.com/rocketscream/Low-Power) i.e. download the whole folder and save it on your disk (i.e. C:\Program Files (x86)\Arduino\libraries). For the low power settings we are following this guide:http://www.home-automation-community.com/arduino-low-power-how-to-run-atmega328p-for-a-year-on-coin-cell-battery/. I.e. to sigificantly reduce power consumption of the pro mini we use the low power command to put the arduino to sleep. The command LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF) sets the arduino to sleep, max time for this is 8 sec after which the arduino just switches on for a couple of mili seconds and goes to sleep again this is reapeated until 1h has passed. Second the power LED of the arduino pro mini was scractched out with a small screw driver. 
We measured during this 1h sleep intervall the arduino draws 0.06mA from the 9V battery and during the on times it draws 18mA. So on average per hour 5.1mA, the 9V battery has about 400mAh that means the 9V battery will only last for about 3 days. The arduino pro mini is also measuring the lead acid battery voltage through a series of large resistors (to keep the current and power consumer by this low) that devide the voltage of the battery into something between 0 and 3.3V such that both the pi and the arduino can read it. If the lead acid batery volatge drops below 11.5V the power to the pi is not switched on to prevent a deep discharge of the lead acid battery.  



Multiplexing and analogue to digital conversion (ADC):
More info on setting up MCP3008: https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
Connect MCP3008 as follows:
* MCP3008 VDD to Raspberry Pi 3.3V
* MCP3008 VREF to Raspberry Pi 3.3V
* MCP3008 AGND to Raspberry Pi GND
MCP3008 DGND to Raspberry Pi GND
MCP3008 CLK to Raspberry Pi pin 18
MCP3008 DOUT to Raspberry Pi pin 23
MCP3008 DIN to Raspberry Pi pin 24
MCP3008 CS/SHDN to Raspberry Pi pin 25
CHannel 0-7 will then read voltages from 0...3.3V and give a signal 0...1023 accordingly 

Sensors:

Data Trasmission:

Data Handling and Display

Mounting and Casing

