from time import sleep

import secrets

import network


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
