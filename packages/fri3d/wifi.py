import network


class Wifi:
    def __init__(self, settings):
        self._wlan = network.WLAN(network.STA_IF)

        try:
            self.essid = settings.get('wifi.essid')
            self.password = settings.get('wifi.password')
            self.reconnects = settings.get('wifi.reconnects')

            print("essid = {}, password = {}, reconnects = {}". format(
                self.essid,
                self.password,
                self.reconnects
            ))
        except Exception as e:
            print("Could not load Wifi settings! " + str(e))

    def connect(self):
        self._wlan.active(True)

        if self._wlan.isconnected():
            return

        print('connecting to network...')
        try:
            self._wlan.config(reconnects=reconnects)
            self._wlan.connect(self.essid, self.password)
        except Exception as e:
            print('Could not connect! ' + str(e))

    
    def is_connected(self):
        return self._wlan.isconnected()

    def disable(self):
        self._wlan.active(False)

    def status(self):
        status = self._wlan.status()
        if status == network.STAT_IDLE:
            return 'idle'
        elif status == network.STAT_CONNECTING:
            return 'connecting'
        elif status == network.STAT_WRONG_PASSWORD:
            return 'wrong password'
        elif status == network.STAT_NO_AP_FOUND:
            return 'no ap found'
        elif status == network.STAT_GOT_IP:
            return 'IP {}'.format(ip())

        return 'error'

    def ip(self):
        return self._wlan.ifconfig()[0]

    def test(self):
        import time
        self.connect()

        while not self.is_connected():
            print('waiting to connect')
            time.sleep(1)

        print('network config:', self._wlan.ifconfig())