#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>

#define LISTEN_PORT 80
 
const char* ssid = "NDL_24G"; //name of local WiFi network in the NDL
const char* password = "RT-AC66U"; 

MDNSResponder mdns;
ESP8266WebServer server(LISTEN_PORT);

bool ledOn = false;

void connectToWifi() {
  WiFi.begin(ssid, password); // Start Wi-Fi connection to specified access point
  Serial.println("Start connecting.");
  while (WiFi.status() != WL_CONNECTED) { // Wait until we are connected
    delay(500);
    Serial.print(".");
  }
 
  Serial.print("Connected to ");
  Serial.print(ssid);
  Serial.print(", IP address: ");
  Serial.println(WiFi.localIP()); // Print local IP to Serial Monitor

  if(mdns.begin("esp8266", WiFi.localIP())) {
    Serial.println("MDNS responder started");
  }
}

void hanleConnection() {
  server.on("/", [](){
    Serial.println("RECEIVED 382u8932784984902384902");
    server.send(200, "text/plain", "Request received!");
  });
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, ledOn); 
  
  connectToWifi();
  hanleConnection();
  server.begin();
  Serial.println("HTTP server started");
}
void loop() {
  server.handleClient(); //Handle all website logic, this should be run every loop!
  mdns.update();
}
