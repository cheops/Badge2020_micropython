from eye import BADGE
import system

def run():
    print("REPL is running.")
    BADGE.display().print_centred(wri, ssd.width//2, ssd.height//2, 'REPL running on USB serial.')
    ssd.show()

    system.show_recover_countdown(5)

run()
