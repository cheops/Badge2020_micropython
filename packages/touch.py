import uasyncio as asyncio
import utime as time
from gui.primitives import launch, Delay_ms

from machine import Pin

class Touch:
    trigger_level = 50
    sample_time = 10
    long_press_ms = 1000
    double_click_ms = 400

    def __init__(self, touch, suppress=False):
        self._touch = touch

    def press_func(self, func=False, args=()):
        self._touch.on_press()

    def release_func(self, func=False, args=()):
        self._rf = func
        self._ra = args

    def double_func(self, func=False, args=()):
        self._df = func
        self._da = args
        if func:  # If double timer already in place, leave it
            if not self._dd:
                self._dd = Delay_ms(self._ddto)
        else:
            self._dd = False  # Clearing down double func

    def long_func(self, func=False, args=()):
        if func:
            if self._ld:
                self._ld.callback(func, args)
            else:
                self._ld = Delay_ms(func, args)
        else:
            self._ld = False

    # Current non-debounced logical button state: True == pressed
    def rawstate(self):
        rel_level =  max(self.touch.read() - self.trigger_level, 0)
        return self.touch.read() < self.trigger_level

    # Return current state of switch (0 = pressed)
    def __call__(self):
        return self.state

    def _ddto(self):  # Doubleclick timeout: no doubleclick occurred
        self._dblpend = False
        if self._supp and not self.state:
            if not self._ld or (self._ld and not self._ld()):
                launch(self._ff, self._fa)

    async def touchcheck(self):
        while True:
            try:
                touched = self.rawstate()
                if touched != self.state:
                    # State has changed: act on it now.
                    self.state = touched
                    if touched == True and self._pf:
                        launch(self._pf, self._pa)
                    elif touched == False and self._rf:
                        launch(self._rf, self._ra)
            except ValueError:
                pass

            await asyncio.sleep_ms(Touch.sample_time)

    def deinit(self):
        self._run.cancel()
