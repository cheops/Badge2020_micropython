from machine import Pin
from neopixel import NeoPixel

neopixel_pin = Pin(2, Pin.OUT)
neopixels = NeoPixel(neopixel_pin, 5)
neopixels[0] = (0,0,0)
neopixels[1] = (0,0,0)
neopixels[2] = (0,0,0)
neopixels[3] = (0,0,0)
neopixels[4] = (0,0,0)
neopixels.write()

