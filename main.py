import time

import machine
from machine import Pin
import onewire
import ds18x20

pin = Pin(27, Pin.IN)
print(pin.value())

one_wire = onewire.OneWire(machine.Pin(pin))
sensor = ds18x20.DS18X20(one_wire)
devices = sensor.scan()

print("Found devices:", devices)
for device in devices:
    while True:
        sensor.convert_temp()
        time.sleep(1)
        temp = sensor.read_temp(device)
        print("Temperature:", temp)
