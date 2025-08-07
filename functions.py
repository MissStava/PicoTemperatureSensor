from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20


def initialise_sensor(pin_number):
    """
    Initialises a DS18X20 temperature sensor on the specified GPIO pin.

    Args:
        pin_number (int): The GPIO pin number to which the sensor is connected.

    Returns:
        DS18X20: An instance of the DS18X20 sensor initialised on the specified pin.
    """

    print("Initialising sensor")

    if pin_number is None:
        raise ValueError("Pin number must be specified to initialise the sensor")

    pin = Pin(pin_number, Pin.IN)
    one_wire = OneWire(pin)
    return DS18X20(one_wire)
