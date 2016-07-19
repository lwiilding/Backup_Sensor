#include <Wire.h>
#include <SoftwareSerial.h>

#define SLAVE_ADDRESS 0x04
int trigPin = 11;    //Trig - green Jumper
int echoPin = 12;    //Echo - yellow Jumper
long duration, cm, inches;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);

  //Define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // define callbacks for i2c communication
  Wire.onRequest(sendData);

  Serial.println("Ready!");
}

void loop() {
  delay(50);
  getBackupData();
}

// callback for sending data
void sendData() {
  Wire.write(cm);
}

void getBackupData(){
  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  // convert the time into a distance
  cm = (duration/2) / 29.1;
  
  Serial.print(cm);
  Serial.print("cm");
  Serial.println();
}


