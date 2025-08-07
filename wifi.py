from time import sleep

import secrets

import network


class WiFi:
    """
    WiFi class for managing wireless network connections on a device.
    Attributes:
        WIFI_CONNECTION_ATTEMPTS (int): Default number of connection attempts.
        WIFI_CONNECTION_WAIT (int): Default wait time (in seconds) for each connection attempt.
    Methods:
        __init__():
            Initializes the WiFi interface and activates it.
        connect(attempts: int = WIFI_CONNECTION_ATTEMPTS, wait: int = WIFI_CONNECTION_WAIT):
            Handles connection attempts, waits for connection, and raises errors for specific
            failure cases.
    """

    WIFI_CONNECTION_ATTEMPTS = 2
    WIFI_CONNECTION_WAIT = 10

    def __init__(self):
        self.wlan = network.WLAN(network.WLAN.IF_STA)
        self.wlan.active(True)

    def connect(
        self, attempts: int = WIFI_CONNECTION_ATTEMPTS, wait: int = WIFI_CONNECTION_WAIT
    ):
        """
        Connects the device to a WiFi network using credentials from the secrets module.

        Args:
            attempts (int): Number of connection attempts.
            wait (int): Seconds to wait for each attempt.
        """

        if self.wlan.isconnected():
            print("Already connected")
            return

        for attempt in range(1, attempts + 1):
            print(f"WiFi attempt {attempt} of {attempts}")
            self.wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

            for _ in range(wait):
                if self.wlan.status() == network.STAT_CONNECTING:
                    print("Connecting...")
                    sleep(1)
                else:
                    break

            status = self.wlan.status()
            if status == network.STAT_GOT_IP:
                print("Network config:", self.wlan.ifconfig())
                return

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
