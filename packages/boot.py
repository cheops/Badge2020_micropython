# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uasyncio

import system
from fri3d import BADGE
from blaster import BLASTER

import sys
sys.path.append('/apps')

# -- enable the accelero to enable backlight
BADGE.accelero()

SYSTEM = system.System(BADGE.settings(), BADGE.display())

def show_recover_countdown(count):
    # bgcolor = wri.bgcolor
    # if (count != 5):
    #     bgcolor = RED
    # display.print_centred(wri, ssd.width//2, ssd.height-20,
    #                       'Hold boot {} seconds to recover.'.format(count), bgcolor=bgcolor)
    # ssd.show()
    pass

async def check_recover_button(pin):
    countdown = 5
    while pin.value() == 0:
        print('Hold for {} seconds to recover main menu.'.format(countdown))
        show_recover_countdown(countdown)
        countdown -= 1
        if countdown == 0:
            SYSTEM.recover()
        await uasyncio.sleep_ms(1000)


# Callback for the boot pin IRQ
def hold_to_recover(pin):
    if pin.value() == 0:
        print("Boot button pressed.")
        # start check task
        uasyncio.run(check_recover_button(pin))


if BADGE.settings().get_or_default('bluetooth.enabled', False):
    BADGE.bluetooth().advertise(BADGE.mac_address())

if BADGE.settings().get_or_default('wifi.enabled', False):
    BADGE.wifi().connect()

app_recover = BADGE.settings().get_or_default('apps.recover', "frozen_apps.eye")
app = BADGE.settings().get_or_default('apps.autorun', app_recover)

BADGE.button().on_press(hold_to_recover)

if app:
    try:
        print("Starting app '{}'...".format(app))
        if app:
            __import__(app)
    except KeyboardInterrupt:
        pass
    except BaseException as e:
        print("Exception happened in app:")
        print(e)
        SYSTEM.recover()


# if application is closed using Ctrl+C on the serial
print("REPL is running.")