import st7789

from machine import SPI, Pin

spi = SPI(2, baudrate=40000000, polarity=1)
pcs = Pin(5, Pin.OUT)
pdc = Pin(33, Pin.OUT)

display = st7789.ST7789(
        spi=spi,
        width=240,
        height=240,
        cs=pcs,
        dc=pdc,
        buffer_size=240 * 240 * 2)
display.init()
