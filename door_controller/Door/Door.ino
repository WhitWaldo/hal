#include <Servo.h> 
#define DELAY 1000
#define DOOR_TRIGGER 72
#define UNLOCK_TRIGGER 73
#define LOCK_TRIGGER 74
#define FINAL_POSITION 130
#define MOTOR_DELAY 5

#define LED_PIN 4
#define MOTOR_PIN 8
#define DOOR_PIN 13
#define OPEN_BUTTON_PIN 10
#define CLOSE_BUTTON_PIN 6
int incomingByte = 0;   // for incoming serial data
Servo myServo;
int pos = 0;
int openButtonState = 0;
int closeButtonState = 0;


void lightOn() {
  digitalWrite(LED_PIN, HIGH);   // turn the LED on (HIGH is the voltage level)             // wait for a second

}
void lightOff() {
  digitalWrite(LED_PIN, LOW);    // turn the LED off by making the voltage LOW
}

void openDoor() {
  lightOn();
  digitalWrite(DOOR_PIN, HIGH);
  delay(1000);
  digitalWrite(DOOR_PIN, LOW);
  lightOff();
}

void unlockDoor() {
  lightOn();
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
  } else {
    delay(200);
  }
  lightOff();
}

void lockDoor() {
  lightOn();
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
  } else {
    delay(200);
  }
  lightOff();
}

void setup() {
  myServo.attach(MOTOR_PIN);
  pinMode(LED_PIN, OUTPUT);
  pinMode(DOOR_PIN, OUTPUT);
  pinMode(OPEN_BUTTON_PIN, INPUT);
  pinMode(CLOSE_BUTTON_PIN, INPUT);
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
    openButtonState = digitalRead(OPEN_BUTTON_PIN);
    if (openButtonState == HIGH) {
        Serial.print("\nopen button: ");
      unlockDoor(); 
    }
    closeButtonState = digitalRead(CLOSE_BUTTON_PIN);
    if (closeButtonState == HIGH) {
      Serial.print("\nclose button: ");
      lockDoor(); 
    }
}
