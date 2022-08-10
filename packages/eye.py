import st7789
import display
from display import color
import uasyncio as asyncio
import random


class Eye:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 70
        self.pupil = 0.5
        self.color = color["GREEN"]

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

        display.display.fill(color["DARK_GREEN"])
        display.display.fill_circle(
            center_x, center_y, self.radius, color["WHITE"])
        display.display.fill_circle(
            int(120 - iris_factor_x), int(120 - iris_factor_y), iris, self.color)
        display.display.fill_circle(int(
            120 - pupil_factor_x), int(120 - pupil_factor_y), int(iris * self.pupil), color["BLACK"])

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


e = Eye()


def run():
    e.auto()

    asyncio.get_event_loop().run_forever()


run()
