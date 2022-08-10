import st7789
from machine import SPI, Pin

def build_display():
    display = st7789.ST7789(
        SPI(2, baudrate=40000000, polarity=1),
        240,
        240,
        reset=Pin(32, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(33, Pin.OUT),
        backlight=Pin(12, Pin.OUT),
        color_order=st7789.RGB,
        inversion=True,
        rotation=0,
        options=0,
        buffer_size=240*240*2)

    display.init()

    return display