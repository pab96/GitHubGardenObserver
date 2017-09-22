# GitHubGardenObserver
Documentation for "Remote Environment Controller for  Experiments in Extreme Environments"

# Project Title




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




Multiplexing and analogue to digital conversion (ADC):
More info on setting up MCP3008: https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
Connect MCP3008 as follows:
MCP3008 VDD to Raspberry Pi 3.3V
MCP3008 VREF to Raspberry Pi 3.3V
MCP3008 AGND to Raspberry Pi GND
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

