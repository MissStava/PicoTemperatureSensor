from time import sleep

import secrets

import network
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20


def connect_to_wifi():
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        while not wlan.isconnected():
            print("Connecting")
            sleep(1)
    print("Network config:", wlan.ipconfig("addr4"))


def initialise_sensor(pin):
    one_wire = OneWire(Pin(pin))
    return DS18X20(one_wire)
