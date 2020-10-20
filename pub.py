#!/usr/bin/python
import sys

import Adafruit_DHT

import datetime

import time

import os

import paho.mqtt.client as mqtt

import httplib, urllib

import Adafruit_DHT

# This is the Publisher

client = mqtt.Client()

client.connect("192.168.1.108",1883,60)

# Define delay between readings

sleep = 0.5 # how many seconds to sleep between posts to the channel  

key = 'MFO60XHZT76DTM48'  # Write API key

humidity, temperature = Adafruit_DHT.read_retry(11, 4)  # GPIO27 (BCM notation)  

#Report Raspberry Pi internal temperature to Thingspeak Channel  

def thermometer():  

  for x in range(15):

        humidity, temperature = Adafruit_DHT.read_retry(11, 4)  # GPIO27 (BCM notation)
        send_Time=datetime.datetime.now()

        sensor_data = ["TEMP = ",(temperature),"HUM = ",(humidity)]

        print 'Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity)

        client.publish("test",str(sensor_data))

        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}  

        conn = httplib.HTTPConnection("api.thingspeak.com:80")  

        try:  

            params = urllib.urlencode({'field1': temperature,'field2': humidity, 'key':key }) # channel name is field1 or field 2

            conn.request("POST", "/update", params, headers)  

            response = conn.getresponse()  
            data = response.read()  


        except:  

            print ("connection failed")  

            break  
  #sleep for desired amount of time
  #time.sleep(sleep)
  conn.close()

  client.disconnect()

if __name__ == "__main__":  

               thermometer()

