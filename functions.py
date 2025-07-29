from time import sleep

import secrets

import network
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20


def connect_to_wifi():
    print("Connecting to WiFi")
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        while not wlan.isconnected():
            print("Connecting")
            sleep(1)
    print("Network config:", wlan.ipconfig("addr4"))


def initialise_sensor(pin):
    print("Initialising sensor")
    one_wire = OneWire(Pin(pin))
    return DS18X20(one_wire)
