#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
// This file is gitignored as it has secrets
// Network SSID and PSWD should be defined in it
#include "secrets.h"

#define BNO055_SAMPLERATE_DELAY_MS 100
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28, &Wire);

const char* server = "192.168.1.60";
const uint16_t port = 50000;
bool is_upside_down = false;
unsigned long upside_down_triggered_at;

WiFiUDP udp;

void connect_to_wifi() {
  WiFi.begin(ssid, password);
  Serial.println("Start connecting.");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.println("Connected to Wifi");
}

void process_event(sensors_event_t event) {
  int z = event.orientation.z;
  int y = event.orientation.y; 

  unsigned long elapsed = millis() - upside_down_triggered_at;
  if (abs(y) > 60 && elapsed >= 4000) {
    is_upside_down = !is_upside_down;
    upside_down_triggered_at = millis();
  }

  if (is_upside_down && (z > 90 || z < -90 || z == 0)) {
    y = -y;
  }
  
  // When upside down we want to treat 180 as starting degree
  if (z > 90) {
    z = -180 + z;
    is_upside_down = true;
  } else if (z < -90) {
    z = 180 + z;
    is_upside_down = true;
  }

  String direction = "Sz:" + String(z) + ",y:" + String(y) + "E";

  udp.beginPacket(server, port);
  udp.write(direction.c_str());
  udp.endPacket();
  
  Serial.println("Sent: " + direction);
}

void setup(void) {
  Serial.begin(115200);
  while (!Serial) delay(10);

  connect_to_wifi();

  if (!bno.begin()) {
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while (1);
  }

  delay(1000);
  bno.setExtCrystalUse(true);
}

void loop(void) {
    sensors_event_t event;
    bno.getEvent(&event);
    process_event(event);
    delay(BNO055_SAMPLERATE_DELAY_MS);
}
