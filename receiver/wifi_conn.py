import wifi
import time

class WiFiConnection:

    def __init__(self):
        self._ssid = "NDL_24G"
        self._password = "RT-AC66U"

    def connect(self):
        self._reset()
        self._scan_networks() # For debugging

        try:
            wifi.radio.connect(self._ssid, self._password, timeout=5)
            print("Connected to", self._ssid, "IP:", wifi.radio.ipv4_address)
            return True
        except ConnectionError as e:
            print("Failed to connect to wifi:", e)
            return False
        except Exception as e:
            print("An unexpected error occurred:", e)
            return False

    # Reset wifi to avoid weird bugs
    def _reset(self):
        wifi.radio.enabled = False
        time.sleep(1)
        wifi.radio.enabled = True

    def _scan_networks(self):
        print("Scanning for WiFi networks...")
        for network in wifi.radio.start_scanning_networks():
            print("SSID:", network.ssid)
            print("Signal strength:", network.rssi)
        wifi.radio.stop_scanning_networks()


