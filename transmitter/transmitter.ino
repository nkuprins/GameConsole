#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <ESP8266WiFi.h>

// Set the delay between fresh samples
#define BNO055_SAMPLERATE_DELAY_MS 100
#define TRIGGER_ANGLE 30
#define DEFAULT_ANGLE 15

// Set the delay between new reconnection attempts
#define RECONNECTION_DELAY_MS 100

Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28, &Wire);

const char* server = "192.168.1.60";
const uint16_t port = 80;
const char* ssid = "NDL_24G";
const char* password = "RT-AC66U"; 

bool in_default = false;

WiFiClient client;

void connectToWifi() {
  WiFi.begin(ssid, password);
  Serial.println("Start connecting.");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.println("Connected to Wifi");
}

void connectToServer() {
  Serial.println("Connecting to server...");
  if (client.connect(server, port)) {
    Serial.println("Connected to server");
  } else {
    Serial.println("Failed to connect to server");
  }
}

void sendDirection(String direction) {
  client.print(direction);
  Serial.println("Sent: " + direction);
}

void checkAndSendDirection(bool triggered, const char* direction) {
  if (triggered) {
    Serial.println(direction);
    sendDirection(direction);
    in_default = false;
  }
}

void process_event(sensors_event_t event) {
  int z = event.orientation.z;
  int y = event.orientation.y;
  
  if (z < DEFAULT_ANGLE && z > -DEFAULT_ANGLE &&
        y < DEFAULT_ANGLE && y > -DEFAULT_ANGLE)
        in_default = true;

  if (!in_default) return;

  checkAndSendDirection(z >= TRIGGER_ANGLE, "LEFT");
  checkAndSendDirection(z <= -TRIGGER_ANGLE, "RIGHT");
  checkAndSendDirection(y >= TRIGGER_ANGLE, "UP");
  checkAndSendDirection(y <= -TRIGGER_ANGLE, "DOWN");
}

void process_event_new(sensors_event_t event) {
  int z = event.orientation.z;
  int y = event.orientation.y; 
  sendDirection("z:" + String(z) + ",y:" + String(y));
}

void setup(void) {
  Serial.begin(115200);
  while (!Serial) delay(10);

  connectToWifi();
  connectToServer();

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
    connectToServer();
    delay(RECONNECTION_DELAY_MS);
  } else {
    sensors_event_t event;
    bno.getEvent(&event);
    process_event(event);
    delay(BNO055_SAMPLERATE_DELAY_MS);
  }
}
