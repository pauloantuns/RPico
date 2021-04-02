#######################################
# This code was developed to use the  #
# NTC 10K thermistor in the Raspberry #
# Pi Pico.                            #
# Paulo Antunes                       #
#######################################

# Based on Arduino NTC project, avalible in:
# https://www.filipeflop.com/blog/termistor-ntc-arduino/

from math import e, log
import machine
from utime import sleep

#Select the analog input of your Pico
#Pico has 3 analog input, GP26 to GP28
ntc = machine.ADC()

#NTC information from datasheet
#This is an MF521033600 NTC
beta = 3600.0 
r0 = 10000.0
t0 = 298.0
rx = r0 * (e**(-beta/t0))

#Circuit information
#The Raspberry Pico has three voltage supply
#VBUS, this one supplies 5V from the USB
#VSYS, this one supplies 1.8 to 5V
#3V3, this one supplies 3.3V
vcc = 3.3
R = 10000 #Parallel resistence

sample = 5

while True:
    sum = 0
    i = 0
    while (i < sample):
        sum += ntc.read_u16()
        i+=1
        sleep(0.01)
    v = (vcc*sum)/(sample*65535)
    rt = (vcc*R)/v - R
    t = beta/(log(rt/rx))
    t_c = t - 273.15
    print(t_c)
    sleep(2)
