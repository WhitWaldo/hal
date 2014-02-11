#include <Servo.h> 
#define DELAY 1000
#define DOOR_TRIGGER 72
#define UNLOCK_TRIGGER 73
#define LOCK_TRIGGER 74
#define ANGLE 90
int incomingByte = 0;   // for incoming serial data
int doorPin = 13;
Servo myServo;
int pos = 0;

void openDoor() {
  digitalWrite(doorPin, HIGH);
  delay(1000);
  digitalWrite(doorPin, LOW);
}

void unlockDoor() {
    for (pos = ANGLE; pos >= 1; pos -= 1) {
        myServo.write(pos);
        delay(15);
    }
}

void lockDoor() {
    for (pos = 0; pos < ANGLE; pos += 1) {
        myServo.write(pos);
        delay(15);
    }
}

void setup() {
  myServo.attach(8);
  pinMode(doorPin, OUTPUT);
  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
}

void loop() {
    // send data only when you receive data:
    if (Serial.available() > 0) {
        // read the incoming byte:
        incomingByte = Serial.read();
        // say what you got:
        Serial.print("I received: ");
        Serial.println(incomingByte, DEC);
        if (incomingByte == DOOR_TRIGGER) {
            openDoor();
        }
        if (incomingByte == LOCK_TRIGGER) {
            lockDoor();
        }
        if (incomingByte == UNLOCK_TRIGGER) {
            unlockDoor();
        }
    }
}

