from prometheus_client import start_http_server, Gauge
import json
import urllib2
import time

# Setup Prometheus metrics.
 
bartemp_metric = Gauge('barometer_sensor_temperature_celcius', 'Barometric sensor temperature reading')
barpres_metric = Gauge('barometer_sensor_pressure_pascals', 'Barometric sensor pressure reading')
humidity_metric = Gauge('humidity_sensor_percent', 'Humidity sensor humidity reading') 
humidity_temp_metric = Gauge('humidity_sensor_temperature_celcius', 'Humidity sensor temperature reading')

if __name__ == '__main__':
    start_http_server(8081)
    while True:
        data = urllib2.urlopen('http://172.30.101.3:8080/temp.json')
        data = json.loads(data.read())

        bartemp_metric.set(data['BarometerTemperature'])
        barpres_metric.set(data['BarometerPressure'])
        humidity_metric.set(data['Humidity'])
        humidity_temp_metric.set(data['HumidityTemperature'])

        time.sleep(60)