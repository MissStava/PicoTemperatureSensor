from time import sleep

from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20


pin = Pin(27, Pin.IN)
print(pin.value())

one_wire = OneWire(Pin(pin))
sensor = DS18X20(one_wire)
devices = sensor.scan()


print("Found devices: ", devices)
for device in devices:
    while True:
        sensor.convert_temp()
        sleep(1)
        temp = sensor.read_temp(device)
        print("Temperature:", temp)
