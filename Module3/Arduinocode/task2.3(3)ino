#include <Servo.h>

const int potPin = A0;
const int ledPin = 8;  
const int servoPin = 9; // Pin PWM untuk servo

Servo myServo;  // Cipta objek servo
bool isHalted = false; // Flag to track halt status

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // 1. Check for incoming serial commands from Python
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'H') {
      digitalWrite(ledPin, HIGH); // Turn LED ON
    } else if (command == 'L') {
      digitalWrite(ledPin, LOW);  // Turn LED OFF
    } else if (command == 'X') {
      isHalted = true;            // Halt Arduino execution/servo updates
    } else if (command == 'R') {
      isHalted = false;           // Resume normal execution
    }
  }

  // If halted by keyboard command, skip potentiometer reading and servo updates
  if (isHalted) {
    digitalWrite(ledPin, LOW); // Turn off LED as visual indicator of halt state
    delay(100);
    return;
  }

  // 2. Read and send potentiometer value to Python
  int potValue = analogRead(potPin);
  Serial.println(potValue);

  // 3. Map potentiometer value to servo angle and update position
  int angle = map(potValue, 0, 1023, 0, 180);
  myServo.write(angle);
  
  delay(100); // Small delay for stability
}
