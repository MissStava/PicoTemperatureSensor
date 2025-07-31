from time import sleep

import secrets

from network import WLAN
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20


def connect_to_wifi():
    """
    Connects the device to a WiFi network using credentials from the secrets module.

    This function activates the WLAN interface in station mode, attempts to connect to
    the WiFi network using the provided SSID and password, and waits until the connection
    is established.
    """

    print("Connecting to WiFi")

    wlan = WLAN(WLAN.IF_STA)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        while not wlan.isconnected():
            print("Connecting")
            sleep(1)

    print("Network config:", wlan.ipconfig("addr4"))


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
