# BLE Beacon for the Fri3dcamp 2020 badge
from micropython import const
import ubluetooth


def _adv_encode(adv_type, value):
    return bytes((len(value) + 1, adv_type)) + value


def _adv_encode_name(name):
    return _adv_encode(const(0x09), name.encode())


class Bluetooth:
    def __init__(self):
        self.bt = ubluetooth.BLE()

    def advertise(self, name):
        while not self.bt.active():
            self.bt.active(True)

        self.bt.gap_advertise(3 * 1000000, _adv_encode(0x01, b'\x06')
                              + _adv_encode_name(name))
