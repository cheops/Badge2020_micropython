import st7789
import uasyncio as asyncio
import random
import color

from fri3d import BADGE


class Eye:
    def __init__(self, display):
        self._display = display
        self.x = 0
        self.y = 0
        self.radius = 70
        self.pupil = 0.5
        self.color = color.GREEN

        self._task = None

    def render(self):
        # -- overwrite the current eye location
        # display.display.fill_circle(self.x, self.y, self.radius, BLACK)

        center_x = 120 - self.x
        center_y = 120 - self.y
        iris = int(self.radius * 0.6)

        offset_factor = 1.5

        iris_factor_x = int(self.x * offset_factor)
        iris_factor_y = int(self.y * offset_factor)

        pupil_factor_x = int(iris_factor_x * offset_factor)
        pupil_factor_y = int(iris_factor_y * offset_factor)

        self._display.fill(color.BLACK)
        self._display.fill_circle(
            center_x, center_y, self.radius, color.WHITE)
        self._display.fill_circle(
            int(120 - iris_factor_x), int(120 - iris_factor_y), iris, self.color)
        self._display.fill_circle(int(
            120 - pupil_factor_x), int(120 - pupil_factor_y), int(iris * self.pupil), color.BLACK)

    def auto(self, enable=True):
        if enable:
            self.task = asyncio.create_task(self._run())
        elif self.task:
            self.task.cancel()

    async def _run(self):
        # display.display.fill(WHITE)
        self.render()
        while True:
            # x , y, z = BADGE.accelero().acceleration
            # print("test", x, y, z)

            self.x = random.randint(-20, 20)
            self.y = random.randint(-20, 20)

            self.render()
            await asyncio.sleep_ms(100)

            await asyncio.sleep_ms(random.randint(3000, 10000))


def wheel(pos, intensity=1.0):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (int((255 - pos * 3) * intensity), int((pos * 3) * intensity), 0)
    if pos < 170:
        pos -= 85
        return (0, int((255 - pos * 3) * intensity), int((pos * 3) * intensity))
    pos -= 170
    return (int((pos * 3) * intensity), 0, int((255 - pos * 3) * intensity))


async def _rainbow(pixels, wait):
    while True:
        for j in range(255):
            for i in range(5):
                rc_index = (i * 256 // 5) + j
                pixels[i] = wheel(rc_index & 255, .5)
            pixels.write()
            await asyncio.sleep_ms(wait)


def run():
    print('Fri3d App is running.')
    print('Ctrl-C to get Python REPL.')

    if BADGE.settings().get_or_default("pixels.rainbow", True):
        asyncio.create_task(_rainbow(BADGE.pixels(), 1))

    e = Eye(BADGE.display())
    e.auto()

    asyncio.get_event_loop().run_forever()

run()
