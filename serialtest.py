import serial
import time


ser=serial.Serial('/dev/ttyUSB0')

time.sleep(5)

ser.write('g')
bartemp = float(ser.readline())
barpres = int(float(ser.readline()))
humidity = int(float(ser.readline()))
humtemp = int(float(ser.readline()))

print "Temperature is %2.2fC, Pressure is %dPa, Humidity is %d percent" %(bartemp,barpres, humidity)


ser.close()

