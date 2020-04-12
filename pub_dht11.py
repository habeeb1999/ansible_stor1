#!/usr/bin/python
import sys
import Adafruit_DHT
import datetime
import time
import os
import paho.mqtt.client as mqtt

# This is the Publisher
client = mqtt.Client()
client.connect("192.168.1.108",1883,60)

# Define delay between readings
delay = 0.5
for x in range(10):
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    send_Time=datetime.datetime.now()
    sensor_data = [(temperature),(humidity)]
    print 'Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity)
    client.publish("test",str(sensor_data))
    #time.sleep(delay)
client.disconnect();

