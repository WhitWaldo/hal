#include <Servo.h> 
#define DELAY 1000
#define DOOR_TRIGGER 72
#define UNLOCK_TRIGGER 73
#define LOCK_TRIGGER 74
#define FINAL_POSITION 130
#define MOTOR_DELAY 5
int incomingByte = 0;   // for incoming serial data
const int doorPin = 13;
const int openButtonPin = 10;
const int closeButtonPin = 6;
Servo myServo;
int pos = 0;
int openButtonState = 0;
int closeButtonState = 0;

void openDoor() {
  digitalWrite(doorPin, HIGH);
  delay(1000);
  digitalWrite(doorPin, LOW);
}

void unlockDoor() {
  Serial.print("\nPosition: ");
  Serial.println(pos, DEC);
  if (pos == 0) {
    for(pos = 0; pos < FINAL_POSITION; pos += 1)  // goes from 0 degrees to 180 degrees 
    {                                  // in steps of 1 degree 
      myServo.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(MOTOR_DELAY);
     // waits 15ms for the servo to reach the position 
    }
    delay(10);
    myServo.write(pos-10); 
  }
}

void lockDoor() {
  Serial.print("\nPosition: ");
  Serial.println(pos, DEC);
  if (pos == FINAL_POSITION) {
    for(pos = FINAL_POSITION; pos>=1; pos-=1)     // goes from 180 degrees to 0 degrees 
    {                                
      myServo.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(MOTOR_DELAY);                       // waits 15ms for the servo to reach the position 
    }
    delay(10);
    myServo.write(pos+10); 
  } 
}

void setup() {
  myServo.attach(8);
  pinMode(doorPin, OUTPUT);
  pinMode(openButtonPin, INPUT);
  pinMode(closeButtonPin, INPUT);
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
    openButtonState = digitalRead(openButtonPin);
    if (openButtonState == HIGH) {
        Serial.print("\nopen button: ");
      unlockDoor(); 
    }
    closeButtonState = digitalRead(closeButtonPin);
    if (digitalRead(closeButtonPin) == HIGH) {
      Serial.print("\nclose button: ");
      lockDoor(); 
    }
}
