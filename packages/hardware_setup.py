# Pushbuttons are wired between the pin and Gnd
# Pico pin  Meaning
# ESP.IO16 Up
# ESP.IO17 Left
# ESP.IO34 Right
# ESP.IO32 Down
# ESP.IO36 Center

from machine import Pin, SPI, freq

import gc
import buttons
from touch import Touch

from drivers.st7789.st7789_4bit import *
SSD = ST7789

spi = SPI(2, baudrate=40000000, polarity=1)
gc.collect()  # Precaution before instantiating framebuf
pcs = Pin(5, Pin.OUT)
pdc = Pin(33, Pin.OUT)
prst = Pin(32, Pin.OUT)
ssd = SSD(spi, height=240, width=240, cs=pcs, dc=pdc, rst=prst)

from gui.core.ugui import Display, Screen

# Define control buttons
prv = Pin(27)
sel = Pin(14)
nxt = Pin(13)

disp = Display(ssd, nxt, sel, prv, touch=50)