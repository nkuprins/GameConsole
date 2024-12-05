import wifi

# This file is git ignored and should be generated
try:
    from properties.secrets import SSID, WIFI_PSWD
except ImportError:
    SSID = "???"
    WIFI_PSWD = "???"
    print("ERROR: secrets are not defined")

class CustomWiFi:

    def connect(self):
        #self._scan_networks()

        try:
            wifi.radio.connect(SSID, WIFI_PSWD, timeout=10)
            print("INFO: Connected to", SSID, "IP - ", wifi.radio.ipv4_address)
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


