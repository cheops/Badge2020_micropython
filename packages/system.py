import machine


class System:
    def __init__(self, settings, display):
        self._settings = settings
        self._display = display

    def start_repl(self):
        print("Executing REPL!")
        self._settings.set('apps.autorun', 'frozen_apps.repl')
        self._settings.store()
        machine.reset()

    def start(self, app):
        self._settings.set('apps.autorun', app)
        self._settings.store()
        machine.reset()

    def recover(self):
        print("Recovering menu!")
        try:
            self._settings.remove('apps.autorun')
        except KeyError:
            # can happen when no apps.autorun is set
            pass
        self._settings.store()
        machine.reset()
