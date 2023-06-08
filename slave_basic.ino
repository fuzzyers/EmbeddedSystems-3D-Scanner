#include <Wire.h>


int received;
void setup() {
  // put your setup code here, to run once:
  Wire.begin(0x12);
  Wire.onRequest(requestEvent);
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
}

void loop() {
  delay(100);
}

void receiveEvent(int bytes) {
  while (Wire.available()) {
    received = Wire.read();
    Serial.println(received);
  }
}

void requestEvent() {
    int valueToSend = received;
    Wire.write(valueToSend);
}
