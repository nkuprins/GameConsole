void setup() {
   pinMode(LED_BUILTIN, OUTPUT); // initialize pin as output
   Serial.begin(9600); // initialize serial communication
   while (!Serial) {
     Serial.println("Waiting");
     delay(100);
   }
   Serial.println("Hello, world!"); // print "Hello, world!" to the serial monitor
}
void loop() {
   digitalWrite(LED_BUILTIN, HIGH); // switch LED on (HIGH voltage)
   delay(1000); // wait 1000 ms, i.e. 1 s
   digitalWrite(LED_BUILTIN, LOW); // switch LED off (LOW voltage)
   delay(1000); // wait a second
   Serial.println("Good morning.");
}
