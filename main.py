from time import sleep

from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20

from wifi import WiFi

PIN_NUMBER = 27


def run_app():
    wifi = WiFi()
    wifi.connect()

    sensor = DS18X20(OneWire(Pin(PIN_NUMBER, Pin.IN)))

    for device in sensor.scan():
        print("Device:", device)
        while True:
            sensor.convert_temp()
            sleep(1)
            temp = sensor.read_temp(device)
            print("Temperature:", temp)


if __name__ == "__main__":
    run_app()
