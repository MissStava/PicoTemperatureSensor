from time import sleep

import secrets

import network
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20

WIFI_CONNECTION_ATTEMPTS = 2
WIFI_CONNECTION_WAIT = 10


def connect_to_wifi(
    attempts: int = WIFI_CONNECTION_ATTEMPTS, wait: int = WIFI_CONNECTION_WAIT
):
    """
    Connects the device to a WiFi network using credentials from the secrets module.

    Args:
        attempts (int): Number of connection attempts.
        wait (int): Seconds to wait for each attempt.
    """

    print("Connecting to WiFi")

    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)

    if wlan.isconnected():
        print("Already connected")
        return wlan

    for attempt in range(1, attempts + 1):
        print(f"WiFi attempt {attempt} of {attempts}")
        wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

        for _ in range(wait):
            if wlan.status() == network.STAT_CONNECTING:
                print("Connecting...")
                sleep(1)
            else:
                break

        status = wlan.status()
        if status == network.STAT_GOT_IP:
            print("Network config:", wlan.ifconfig())
            return wlan

        if status == network.STAT_WRONG_PASSWORD:
            print("Connection failed: Wrong WiFi password.")
            raise RuntimeError("Wrong WiFi password")

        if status == network.STAT_NO_AP_FOUND:
            print("Connection failed: Access point not found.")
            raise RuntimeError("Access point not found")

        print("Connection failed.")
        sleep(1)

    print("Failed to connect to WiFi.")
    raise RuntimeError("Failed to connect to WiFi")


def initialise_sensor(pin):
    """
    Initialises a DS18X20 temperature sensor on the specified GPIO pin.

    Args:
        pin (int): The GPIO pin number to which the sensor is connected.

    Returns:
        DS18X20: An instance of the DS18X20 sensor initialised on the specified pin.
    """

    print("Initialising sensor")

    one_wire = OneWire(Pin(pin))

    return DS18X20(one_wire)
