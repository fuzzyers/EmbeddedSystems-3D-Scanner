/*
 * @file: arduinopi.ino
 * @description : This file revolves around allowing the arduino to send
 * and recieve data with the raspberry pi along with also 
 * controlling the stepper motor for the turntable.
 * @author: Jackson Williamson
 * @lastedit: 09/06/2023
 */

Wire library handles the i2c communication for the arduino
#include <Wire.h>
#include <Stepper.h>

const int stepsPerRevolution = 200;
const int motorSpeed = 60;
int received = 1;

/*
 * We have created a new instance of Stepper with the name of stepper
 * it is created with steps to set its steps per revolution
 * along with being set to pins 8, 9, 10, 11
 */
Stepper stepper(stepsPerRevolution, 8, 9, 10, 11);

/*
 * The setup function will intialise mutliple factors
 * Wire.begin(0x12); This intialises the I2C communication at the
 * address of 0x12 to allow Raspberry Pi (master) and arduino (slave) communication.
 * Wire.onRequest will execute code in the request event function
 * when the Raspberry Pi Calls for data.
 * Wire.onReceive will execute the function receiveEvent when receiving from 
 * the Raspberry Pi.
 * Serial.begin just intiallizes the serial communication on 9600
 * stepper gets ret to a speed of 60 (motorspeed) rpm
 */
void setup() {
  //Wire.begin(0x12);
  //Wire.onRequest(requestEvent);
  //Wire.onReceive(receiveEvent);
  Serial.begin(9600);
  stepper.setSpeed(motorSpeed);
}

void loop() {
  if (received == 1){
    motor();
  }
  delay(100);
}

/*
 * The recieveEvent function will run aslong as Wire.available is returning true it will then
 * save what is read over wire into a variable called received and then print out received to 
 * the serial terminal
 */
void receiveEvent(int bytes) {
   while (Wire.available()) {
     received = Wire.read();
     Serial.println(received);
   }
 }

/*
 * The requestEvent triggers when the raspberry pi wants to recieve
 * data in this case its just returning what has been sent by the pi
 */
void requestEvent() {
    int valueToSend = received;
    Wire.write(valueToSend);
}

void motor() {
  stepper.step(stepsPerRevolution);

  Serial.println("test");
}
