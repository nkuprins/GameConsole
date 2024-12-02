import wifi
from properties.constants import SSID, WIFI_PSWD

class CustomWiFi:

    def __init__(self):
        self._ssid = SSID
        self._password = WIFI_PSWD

    def connect(self):
        #self._scan_networks()

        try:
            wifi.radio.connect(self._ssid, self._password, timeout=10)
            print("INFO: Connected to", self._ssid, "IP - ", wifi.radio.ipv4_address)
            return True
        except ConnectionError as e:
            print("ERROR: Failed to connect to wifi - ", e)
            return False

    # Only for debugging to check if hardware works
    def _scan_networks(self):
        print("DEBUG: Scanning for WiFi networks...")
        for network in wifi.radio.start_scanning_networks():
            print("DEBUG: SSID - ", network.ssid)
            print("DEBUG: Signal strength - ", network.rssi)
        wifi.radio.stop_scanning_networks()


