import json
import csv
import urllib2
import time
import gzip
import os

if os.path.isdir("data/") == False:
    os.mkdir("data/")

tijd = time.localtime()
strtijd = "%d%02d%02d" %(tijd.tm_year,tijd.tm_mon,tijd.tm_mday)

tempfile = gzip.open('data/temp-'+strtijd+'.csv.gz','wb')
tempcsv = csv.writer(tempfile,delimiter=',')

tempcsv.writerow(['time','Barometer Temperature','Barometer Pressure','Humidity','Humidity Temperature'])

while True:
    try:
        tijd = time.localtime()
        if(strtijd != "%d%02d%02d" %(tijd.tm_year,tijd.tm_mon,tijd.tm_mday)):
            tempfile.close()
            strtijd = "%d%02d%02d" %(tijd.tm_year,tijd.tm_mon,tijd.tm_mday)
            tempfile = gzip.open('data/temp-'+strtijd+'.csv.gz','wb')
            tempcsv = csv.writer(tempfile,delimiter=',')
            tempcsv.writerow(['time','Barometer Temperature','Barometer Pressure','Humidity','Humidity Temperature'])

        data = urllib2.urlopen('http://172.30.101.3:8080/temp.json')
        data = json.loads(data.read())
        tempcsv.writerow([data['CurrentTime'],data['BarometerTemperature'],data['BarometerPressure'],data['Humidity'],data['HumidityTemperature']])
        print "The temperature is %2.2fC at %ds" %(data['BarometerTemperature'],data['CurrentTime'])
        time.sleep(60)
    except KeyboardInterrupt:
        print "Shutting down"
        tempfile.close()
        break