#define DELAY 1000
#define TRIGGER 72

int incomingByte = 0;   // for incoming serial data
int doorPin = 13;

void openDoor() {
  digitalWrite(doorPin, HIGH);
  delay(1000);
  digitalWrite(doorPin, LOW);
}

void setup() {
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
    if (incomingByte == TRIGGER)  {
      openDoor();
    }
  }
}

