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

color = {
        "BLACK": st7789.BLACK,
        "BLUE": st7789.BLUE,
        "RED": st7789.RED,
        "GREEN": st7789.GREEN,
        "CYAN": st7789.CYAN,
        "MAGENTA": st7789.MAGENTA,
        "YELLOW": st7789.YELLOW,
        "WHITE": st7789.WHITE,
        "DARK_GREEN": 0x03E0
}
