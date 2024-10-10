#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (100)

Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28, &Wire);

const char* server = "http://192.168.1.35";
const char* ssid = "NDL_24G";
const char* password = "RT-AC66U"; 

bool inPos = false;

WiFiClient client;
HTTPClient http;

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
  /* Get the system status values (mostly for debugging purposes) */
  uint8_t system_status, self_test_results, system_error;
  system_status = self_test_results = system_error = 0;
  bno.getSystemStatus(&system_status, &self_test_results, &system_error);

  /* Display the results in the Serial Monitor */
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
  /* Get the four calibration values (0..3) */
  /* Any sensor data reporting 0 should be ignored, */
  /* 3 means 'fully calibrated" */
  uint8_t system, gyro, accel, mag;
  system = gyro = accel = mag = 0;
  bno.getCalibration(&system, &gyro, &accel, &mag);

  /* The data should be ignored until the system calibration is > 0 */
  Serial.print("\t");
  if (!system)
  {
    Serial.print("! ");
  }

  /* Display the individual values */
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
  WiFi.begin(ssid, password); // Start Wi-Fi connection to specified access point
  Serial.println("Start connecting.");
  while (WiFi.status() != WL_CONNECTED) { // Wait until we are connected
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.println("Connected to Wifi");
}

void sendHttpRequest() {
  if (WiFi.status() == WL_CONNECTED) {
//    String url = String(server) + "/?direction=" + direction;
    String url = String(server) + "/";
    http.begin(client, url);
    int httpCode = http.GET();
    if (httpCode > 0) { 
      String payload = http.getString();
      Serial.println(payload); 
    } else {
      Serial.printf("Error in HTTP request: %d\n", httpCode);
    }
    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }
}

void checkPos(sensors_event_t event) {

  int z = event.orientation.z;
  int y = event.orientation.y;

  if (z < 15 && z > -15) {
    inPos = false;
  }

  if (inPos) {
    return;
  }
  
  
  if (z >= 30) {
    Serial.println("LEFT");
    sendHttpRequest();
    inPos = true;
  } else if (z <= -30) {
    Serial.println("RIGHT");
    sendHttpRequest();
    inPos = true;
  }
}



void setup(void)
{
  Serial.begin(115200);

  while (!Serial)
    delay(10);

  connectToWifi();

  Serial.println("Orientation Sensor Test"); 
  Serial.println("");

  if(!bno.begin())
  {
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }

  delay(1000);

  displaySensorDetails();
  displaySensorStatus();

  bno.setExtCrystalUse(true);
}

void loop(void)
{
  sensors_event_t event;
  bno.getEvent(&event);
  
  // z: 30 then LEFT
  // z: -30 then RIGHT
  // y: 30 then UP
  // y: -30 then DOWN
  
  checkPos(event);

  

//  Serial.print("X: ");
//  Serial.print(event.orientation.x, 4);
//  Serial.print("\tY: ");
//  Serial.print(event.orientation.y, 4);
//  Serial.print("\tZ: ");
//  Serial.print(event.orientation.z, 4);

//  displayCalStatus();

  /* Optional: Display sensor status (debug only) */
  //displaySensorStatus();

  delay(BNO055_SAMPLERATE_DELAY_MS);
}
