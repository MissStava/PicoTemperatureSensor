from time import sleep

import functions
from wifi import WiFi

PIN_NUMBER = 27


def run_app():
    wifi = WiFi()
    wifi.connect()

    sensor = functions.initialise_sensor(PIN_NUMBER)

    for device in sensor.scan():
        print("Device:", device)
        while True:
            sensor.convert_temp()
            sleep(1)
            temp = sensor.read_temp(device)
            print("Temperature:", temp)


if __name__ == "__main__":
    run_app()
