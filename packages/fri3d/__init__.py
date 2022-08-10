from machine import Pin
from neopixel import NeoPixel

from fri3d import pinout
from fri3d.settings import Settings

MAC_OFFSET = 2

__all__ = ['Fri3d', 'BADGE']


class Fri3d:
    def __init__(self):
        self._i2c = None
        self._accelero = None
        self._bluetooth = None
        self._buzzer = None
        self._button = None
        self._touch = None
        self._display = None
        self._wifi = None
        self._gui = None
        self._pixels = NeoPixel(Pin(pinout.neopixels, Pin.OUT), 5)
        for idx in range(5):
            self._pixels[idx] = (0,0,0)

        self._battery_charging = Pin(pinout.battery_charging, Pin.IN)
        self._battery_level = Pin(pinout.battery_level, Pin.IN)

        # -- load the settings
        self._settings = Settings()
        self._settings.load()

    def settings(self):
        return self._settings

    def is_charging(self):
        return self._battery_charging.value()

    def battery_level(self):
        return self._battery_level.value()

    def i2c(self):
        if not self._i2c:
            from machine import I2C
            self._i2c = I2C(scl=Pin(pinout.i2c_scl), sda=Pin(pinout.i2c_sda))

        return self._i2c

    def accelero(self):
        if not self._accelero:
            from lis2hh12 import LIS2HH12
            self._accelero = LIS2HH12(self.i2c(), address=pinout.accelero_address)
            self._accelero.enable_act_int()

            # i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
            # imu = LIS2HH12(i2c, address=0x18, sf=SF_G)
            # # enable the ACC interrupt to turn on backlight
            # imu.enable_act_int()

        return self._accelero

    def gui(self):
        if not self._gui:
            from fri3d.gui import Gui
            self._gui = Gui(self.display(), self.touch())

        return self._gui

    def pixels(self):
        return self._pixels

    def buzzer(self):
        if not self._buzzer:
            from fri3d.buzzer import Buzzer
            self._buzzer = Buzzer(pinout.buzzer)

        return self._buzzer

    def bluetooth(self):
        if not self._bluetooth:
            from fri3d.bluetooth import Bluetooth
            self._bluetooth = Bluetooth()

        return self._bluetooth

    def button(self):
        if not self._button:
            from fri3d.buttons import Button
            self._button = Button(pinout.button)

        return self._button

    def touch(self):
        if not self._touch:
            from machine import TouchPad
            from fri3d.touch import NiftyTouch
            self._touch = [NiftyTouch(TouchPad(Pin(x)), idx, self.pixels()) for idx, x in enumerate(pinout.touch)]

        return self._touch

    def display(self):
        if not self._display:
            from fri3d.display import build_display
            self._display = build_display()

        return self._display

    def mac_address(self):
        from machine import unique_id
        base_mac_address = unique_id()
        mac_address = list(base_mac_address[:-1])
        mac_address.append(base_mac_address[-1] + MAC_OFFSET)
        return ':'.join('%02X' % b for b in mac_address)

    def wifi(self):
        if not self._wifi:
            from fri3d.wifi import Wifi
            self._wifi = Wifi(self.settings())

        return self._wifi


BADGE = Fri3d()