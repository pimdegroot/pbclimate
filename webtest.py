#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import serial
import time
import json

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        if self.path=="/temp.json":
            ser.write('g')
            bartemp = float(ser.readline())
            barpres = int(float(ser.readline()))
            humidity = int(float(ser.readline()))
            humtemp = int(float(ser.readline()))
            currenttime = time.time()

            data = {'BarometerTemperature':bartemp, 'BarometerPressure':barpres, 'Humidity':humidity, 'HumidityTemperature':humtemp, 'CurrentTime':int(currenttime)}

            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            # Send the html message
            self.wfile.write(json.dumps(data))
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