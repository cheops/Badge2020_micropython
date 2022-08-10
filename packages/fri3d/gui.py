from gui.core.ugui import Display, Screen


class Gui:
    def __init__(self, display, touch_buttons):
        self._gui = Display(display, input=TouchInput(touch_buttons[0], touch_buttons[1], touch_buttons[2]))

    def display(self):
        return self._gui


class TouchInput:
    def __init__(self, prv, sel, nxt):
        self._prev = prv
        self._sel = sel
        self._next = nxt

        self._prev.on_press(Screen.ctrl_move, (const(2),))
        self._sel.on_release(Screen.sel_ctrl)
        self._next.on_press(Screen.ctrl_move, (const(1),))

    def precision(self, val):
        Screen.redraw_co()

    def adj_mode(self, v=None):
        Screen.redraw_co()

    def is_adjust(self):
        return False


