from time import sleep

from machine import Pin

import functions


functions.connect_to_wifi()
pin = Pin(27, Pin.IN)
sensor = functions.initialise_sensor(pin)

for device in sensor.scan():
    print("Device:", device)
    while True:
        sensor.convert_temp()
        sleep(1)
        temp = sensor.read_temp(device)
        print("Temperature:", temp)
