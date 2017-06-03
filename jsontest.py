import serial
import time
import json

ser=serial.Serial('/dev/ttyUSB0')

time.sleep(2)

ser.write('g')
bartemp = float(ser.readline())
barpres = int(float(ser.readline()))
humidity = int(float(ser.readline()))
humtemp = int(float(ser.readline()))
currenttime = time.time()

print "Temperature is %2.2fC, Pressure is %dPa, Humidity is %d percent at %ds" %(bartemp,barpres, humidity,currenttime)

data = {'BarometerTemperature':bartemp, 'BarometerPressure':barpres, 'Humidity':humidity, 'HumidityTemperature':humtemp, 'CurrentTime':int(currenttime)}
print data
print json.dumps(data)

ser.close()

