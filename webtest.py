#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from prometheus_client import Gauge
import serial
import time
import json

PORT_NUMBER = 8080

# Setup Prometheus metrics.
bartem_metric = Gauge('barometer_sensor_temperature_celcius', 'Barometric sensor temperature reading')
barpres_metric = Gauge('barometer_sensor_pressure_pascals', 'Barometric sensor pressure reading')
humidity_metric = Gauge('humidity_sensor_percent', 'Humidity sensor humidity reading')
humidity_temp_metric = Gauge('humidity_sensor_temperature_celcius', 'Humidity sensor temperature reading')

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        ser.write('g')
        bartemp = float(ser.readline())
        barpres = int(float(ser.readline()))
        humidity = int(float(ser.readline()))
        humtemp = int(float(ser.readline()))
        currenttime = time.time()

        bartemp_metric.set(bartemp)
        barpres_metric.set(barpres)
        humidity_metric.set(humidity)
        humidity_temp_metric.set(humtemp)

        if self.path=="/temp.json":
            data = {'BarometerTemperature':bartemp, 'BarometerPressure':barpres, 'Humidity':humidity, 'HumidityTemperature':humtemp, 'CurrentTime':int(currenttime)}

            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            # Send the html message
            self.wfile.write(json.dumps(data))
            return
        elif self.path=="/metrics":
            registry = core.REGISTRY
            params = parse_qs(urlparse(self.path).query)
            if 'name[]' in params:
                registry = registry.restricted_registry(params['name[]'])
            try:
                output = generate_latest(registry)
            except:
                self.send_error(500, 'error generating metric output')
                raise
            self.send_response(200)
            self.send_header('Content-Type', CONTENT_TYPE_LATEST)
            self.end_headers()
            self.wfile.write(output)
            return
        else:
            self.send_error(404,'File Not Found: %s' % self.path)

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
    
    ser=serial.Serial('/dev/ttyUSB0')
    time.sleep(2)

    #Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
    ser.close()
