#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <ESP8266WiFi.h>

/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (100)

Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28, &Wire);

const char* server = "192.168.1.60";
const uint16_t port = 80;
const char* ssid = "NDL_24G";
const char* password = "RT-AC66U"; 

bool inPos = false;

WiFiClient client;

/**************************************************************************/
/*
    Displays some basic information on this sensor from the unified
    sensor API sensor_t type (see Adafruit_Sensor for more information)
*/
/**************************************************************************/
void displaySensorDetails(void)
{
  sensor_t sensor;
  bno.getSensor(&sensor);
  Serial.println("------------------------------------");
  Serial.print  ("Sensor:       "); Serial.println(sensor.name);
  Serial.print  ("Driver Ver:   "); Serial.println(sensor.version);
  Serial.print  ("Unique ID:    "); Serial.println(sensor.sensor_id);
  Serial.print  ("Max Value:    "); Serial.print(sensor.max_value); Serial.println(" xxx");
  Serial.print  ("Min Value:    "); Serial.print(sensor.min_value); Serial.println(" xxx");
  Serial.print  ("Resolution:   "); Serial.print(sensor.resolution); Serial.println(" xxx");
  Serial.println("------------------------------------");
  Serial.println("");
  delay(500);
}

/**************************************************************************/
/*
    Display some basic info about the sensor status
*/
/**************************************************************************/
void displaySensorStatus(void)
{
  uint8_t system_status, self_test_results, system_error;
  system_status = self_test_results = system_error = 0;
  bno.getSystemStatus(&system_status, &self_test_results, &system_error);

  Serial.println("");
  Serial.print("System Status: 0x");
  Serial.println(system_status, HEX);
  Serial.print("Self Test:     0x");
  Serial.println(self_test_results, HEX);
  Serial.print("System Error:  0x");
  Serial.println(system_error, HEX);
  Serial.println("");
  delay(500);
}

/**************************************************************************/
/*
    Display sensor calibration status
*/
/**************************************************************************/
void displayCalStatus(void)
{
  uint8_t system, gyro, accel, mag;
  system = gyro = accel = mag = 0;
  bno.getCalibration(&system, &gyro, &accel, &mag);

  Serial.print("\t");
  if (!system)
  {
    Serial.print("! ");
  }

  Serial.print("Sys:");
  Serial.print(system, DEC);
  Serial.print(" G:");
  Serial.print(gyro, DEC);
  Serial.print(" A:");
  Serial.print(accel, DEC);
  Serial.print(" M:");
  Serial.print(mag, DEC);
}

void connectToWifi() {
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.println("Connected to WiFi");
}

void connectToServer() {
  if (!client.connected()) {
    Serial.println("Connecting to server...");
    if (client.connect(server, port)) {
      Serial.println("Connected to server");
    } else {
      Serial.println("Failed to connect to server");
    }
  }
}

void sendDirection(String direction) {
  if (client.connected()) {
    client.print(direction);
    Serial.println("Sent: " + direction);
  }
}

void checkPos(sensors_event_t event) {
  int z = event.orientation.z;

  if (z < 15 && z > -15) {
    inPos = false;
  }

  if (inPos) {
    return;
  }
  
  if (z >= 30) {
    Serial.println("LEFT");
    sendDirection("LEFT");
    inPos = true;
  } else if (z <= -30) {
    Serial.println("RIGHT");
    sendDirection("RIGHT");
    inPos = true;
  }
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

  displaySensorDetails();
  displaySensorStatus();

  bno.setExtCrystalUse(true);
}

void loop(void) {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Reconnecting to WiFi...");
    connectToWifi();
  }
  if (!client.connected()) {
    connectToServer();
  }

  sensors_event_t event;
  bno.getEvent(&event);

  checkPos(event);

  delay(BNO055_SAMPLERATE_DELAY_MS);
}
