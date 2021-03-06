SLEEP_TIME = 100 / 1000

MINIMUM_MESSAGE_SIZE = 6
MAXIMUM_MESSAGE_SIZE = MINIMUM_MESSAGE_SIZE + 8

START_BYTE = 0x0F
END_BYTE = 0x04

HIGH_PRIORITY = 0xF8
FIRMWARE_PRIORITY = 0xF9
THIRD_PARTY_PRIORITY = 0xFA
LOW_PRIORITY = 0xFB
PRIORITY = [HIGH_PRIORITY, FIRMWARE_PRIORITY, THIRD_PARTY_PRIORITY, LOW_PRIORITY]

LOW_ADDRESS = 0x00
HIGH_ADDRESS = 0xFF

RTR = 0x40
NO_RTR = 0x00

ENERGY_KILO_WATT_HOUR: str = "kWh"
ENERGY_WATT_HOUR: str = "Wh"
VOLUME_CUBIC_METER: str = "m3"  # Not an official constant at HA yet
VOLUME_CUBIC_METER_HOUR: str = "m3/h"  # Not an official constant at HA yet
VOLUME_LITERS: str = "L"
VOLUME_LITERS_HOUR: str = "L/h"  # Not an official constant at HA yet
