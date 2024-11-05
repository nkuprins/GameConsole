import wifi

class WiFiConnection:

    def __init__(self):
        self._ssid = "NDL_24G"
        self._password = "RT-AC66U"

    def connect(self):   
    	self._reset()

        try:
            wifi.radio.connect(self.ssid, self.password, timeout=5)
            print("Connected to", self.ssid, "IP:", wifi.radio.ipv4_address)
            return True
        except ConnectionError as e:
            print("Failed to connect:", e)
            return False
        except Exception as e:
            print("An unexpected error occurred:", e)
            return False

    # Reset wifi to avoid weird bugs
    def _reset(self):
        wifi.radio.enabled = False
        time.sleep(1)
        wifi.radio.enabled = True