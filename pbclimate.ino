#include <Wire.h>
#include <Adafruit_BMP085.h>
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);


Adafruit_BMP085 bmp;

  
void setup() {
  Serial.begin(9600);
  dht.begin();
  bmp.begin();
}
  
void loop() {
  if(Serial.available() > 0){
    char inchar = (char)Serial.read();
    if(inchar == 'g'){
      Serial.println(bmp.readTemperature());
      Serial.println(bmp.readPressure());
      Serial.println(dht.readHumidity());
      Serial.println(dht.readTemperature());
    }
  }

    
    // Calculate altitude assuming 'standard' barometric
    // pressure of 1013.25 millibar = 101325 Pascal

  // you can get a more precise measurement of altitude
  // if you know the current sea level pressure which will
  // vary with weather and such. If it is 1015 millibars
  // that is equal to 101500 Pascals.
    
    
    
}
