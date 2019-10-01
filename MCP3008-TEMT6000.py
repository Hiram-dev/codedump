import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1350000

def ReadChannel(channel):
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1]&3) << 8) + adc[2]
	return data

def ConvertVolts(data,places):
	volts = (data*3.3)/float(1023)
	volts = round(volts,places)
	amps = volts/10000
	microamps = amps*1000000
	lux = microamps*2
	return lux


while True:
	output = ReadChannel(0)
	lux = ConvertVolts(output,2)
	print(lux)
	time.sleep(1)
