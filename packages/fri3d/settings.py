# Read and change the configuration of the Fri3dcamp badge

import json

FILENAME = '/settings.json'

DEFAULT_SETTINGS = {}


class Settings:
    def __init__(self):
        self.current = None

    def load(self):
        try:
            with open(FILENAME, 'r') as f:
                self.current = json.load(f)
        except Exception as e:
            print(e, type(e))
            print('Could not read settings; reverting to defaults')
            self.save(DEFAULT_SETTINGS)
            self.current = DEFAULT_SETTINGS

        print('Loaded settings: ' + json.dumps(self.current))

    def store(self):
        self.save(self.current)

    def save(self, settings):
        f = open(FILENAME, 'w')
        json.dump(settings, f)
        f.close()

        print('Saved settings: ' + json.dumps(settings))

    def items(self):
        return self.current.items()

    def set(self, key, value):
        sub_next = self.current
        try:
            for k in key.split('.'):
                sub = sub_next
                last_key = k
                if k not in sub:
                    sub[k] = {}
                sub_next = sub[k]
        except KeyError:
            pass

        sub[last_key] = value

    def get(self, key):
        sub = self.current
        try:
            for k in key.split('.'):
                sub = sub[k]
        except KeyError:
            return None

        return sub

    def get_or_default(self, key, default_value):
        sub = self.current
        try:
            for k in key.split('.'):
                sub = sub[k]
        except KeyError:
            self.set(key, default_value)
            self.store()
            return default_value

        return sub

    def remove(self, key):
        sub_next = self.current
        try:
            for k in key.split('.'):
                sub = sub_next
                last_key = k
                sub_next = sub[k]
        except KeyError:
            pass

        del sub[last_key]