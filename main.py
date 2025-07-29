from time import sleep

from machine import Pin

import functions


def run_app():
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


if __name__ == "__main__":
    run_app()
