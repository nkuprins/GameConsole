#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <ESP8266WiFi.h>
// This file is gitignored as it has secrets
// Network SSID and PSWD should be defined
#include "secrets.h"

#define BNO055_SAMPLERATE_DELAY_MS 200
#define RECONNECTION_DELAY_MS 100

Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28, &Wire);

const char* server = "192.168.1.60";
const uint16_t port = 80;

WiFiClient client;

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

void connect_to_server() {
  Serial.println("Connecting to server...");
  if (client.connect(server, port)) {
    Serial.println("Connected to server");
  } else {
    Serial.println("Failed to connect to server");
  }
}

bool is_upside_down = false;

void process_event(sensors_event_t event) {
  int z = event.orientation.z;
  int y = event.orientation.y; 

  if (abs(y) > 70) {
    is_upside_down = !is_upside_down;
  }

  if (is_upside_down || z > 90 || z < -90) {
    y = -y;
  }
  
  // When upside down we want to treat 180 as starting degree
  if (z > 90) {
    z = -180 + z;
  } else if (z < -90) {
    z = 180 + z;
  }

  String direction = "Sz:" + String(z) + ",y:" + String(y) + "E";
  client.print(direction);
  Serial.println("Sent: " + direction);
}

void setup(void) {
  Serial.begin(115200);
  while (!Serial) delay(10);

  connect_to_wifi();
  connect_to_server();

  Serial.println("Orientation Sensor Test"); 
  Serial.println("");

  if (!bno.begin()) {
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while (1);
  }

  delay(1000);
  bno.setExtCrystalUse(true);
}

void loop(void) {
  if (!client.connected()) {
    connect_to_server();
    delay(RECONNECTION_DELAY_MS);
  } else {
    sensors_event_t event;
    bno.getEvent(&event);
    process_event(event);
    delay(BNO055_SAMPLERATE_DELAY_MS);
  }
}
