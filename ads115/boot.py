from machine import I2C, Pin
from ads1x15 import *
i2c = I2C( sda = Pin(4), scl=Pin(5) )
adc = ADS1115(i2c = i2c, address = 72, gain = 0)

def convert(v):
    return v * 0.1875 / 1000

for i in range(4):
    value = adc.read( rate=0, channel1=i )
    print( "ADC%s = %s" % (i, convert(value)))
