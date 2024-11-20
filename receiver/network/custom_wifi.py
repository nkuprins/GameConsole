import wifi
import time
from utility import SSID, WIFI_PSWD

# Class to set up wifi connection
class CustomWiFi:

    def __init__(self):
        self._ssid = SSID
        self._password = WIFI_PSWD

    def connect(self):
        self._reset()
        self._scan_networks()

        try:
            wifi.radio.connect(self._ssid, self._password, timeout=5)
            print("INFO: Connected to", self._ssid, "IP - ", wifi.radio.ipv4_address)
            return True
        except ConnectionError as e:
            print("ERROR: Failed to connect to wifi - ", e)
            return False
        except Exception as e:
            print("ERROR: An unexpected error occurred - ", e)
            return False

    # Reset WiFi to avoid weird bugs
    def _reset(self):
        wifi.radio.enabled = False
        time.sleep(1)
        wifi.radio.enabled = True

    # Only for debugging to check if hardware works
    def _scan_networks(self):
        print("DEBUG: Scanning for WiFi networks...")
        for network in wifi.radio.start_scanning_networks():
            print("DEBUG: SSID - ", network.ssid)
            print("DEBUG: Signal strength - ", network.rssi)
        wifi.radio.stop_scanning_networks()


